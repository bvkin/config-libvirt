import libvirt
import sys


def get_libvirt_env_state(connection):
    conn = libvirt.open(connection)

    if conn == None:
        print('Failed to open connection')
        exit(1)

    domains = conn.listAllDomains(0)

    domain_names = [dom.name() for dom in domains]
    domain_states = [dom.isActive() for dom in domains]

    domain_data = {
        name: {
            'state': state
        }
        for name,
        state in zip(domain_names, domain_states)
    }

    return domain_data


class FilterModule(object):
    ''' Filters to handle openshift_cluster_content data '''

    def filters(self):
        return {
            'get_libvirt_env_state': get_libvirt_env_state
        }
