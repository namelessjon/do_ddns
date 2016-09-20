import requests
import click
import sys

def p(*args, **kwargs):
    click.echo(*args, **kwargs)

def get_ip():
    r = requests.get('https://api.ipify.org?format=random')
    if r.status_code == 200:
        return r.text
    else:
        p("Failed to find IP:{}".format(r.text))
        sys.exit(1)



def get_a_record(domain, api_key):
    r = requests.get('https://api.digitalocean.com/v2/domains/{}/records'.format(domain), auth = (api_key, ''))
    if r.status_code == 200:
        do_domain_info = r.json()
        A = [record for record in do_domain_info['domain_records'] if record['type'] == 'A'  ]
        return A[0]
    else:
        p("Problem fetching DO domains: {}".format(r.text))
        sys.exit(1)

def update_a_record(domain, api_key, record_id, ip):
    r = requests.put('https://api.digitalocean.com/v2/domains/{}/records/{}'.format(domain, record_id), auth=(api_key, ''), json={'data': ip})
    if r.status_code == 200:
        return True
    else:
        p("Problem updating DO domain: {}".format(r.text))
        sys.exit(1)

@click.command()
@click.option('--domain', required=True, help = "The domain to manage")
@click.option('--api-key', required=True, help = "Your DigitalOcean API key")
def update_dns(domain, api_key):
    ip = get_ip()
    a_record = get_a_record(domain, api_key)

    if a_record['data'] == ip:
        p("IP up to date ({})".format(ip))
    else:
        p("Existing IP: {}, new IP: {}".format(a_record['data'], ip))
        if update_a_record(domain, api_key, a_record['id'], ip) is True:
            p("IP successfully updated")
    sys.exit(0)


if __name__ == '__main__':
    update_dns(auto_envvar_prefix='DO_DDNS')
