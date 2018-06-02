#!/usr/bin/python

import re
from ansible.module_utils.basic import *


def main():
    module = AnsibleModule(
        argument_spec=dict(
            configured_disk=dict(type='str', required=True),
        ),
        # Check mode don't differ from a "real" run.
        supports_check_mode=True
    )

    disk = module.params['configured_disk']

    if disk:
        pattern = re.compile("\/dev\/[s,v]d[a-z]")
        if not pattern.match(disk):
            module.fail_json(msg=str(disk) + " is not a valid disk")
        module.exit_json(changed=False)
    else:
        module.fail_json(msg="The parameter backup_disk has no value defined")


if __name__ == '__main__':
    main()
