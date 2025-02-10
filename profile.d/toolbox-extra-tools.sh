#! /usr/bin/env bash

_tet_vm_enter_completion() {
    # List all podman containers
    local containers
    containers=$(podman ps -a --format '{{.Names}}')

    # Completion list
    COMPREPLY=($(compgen -W "${containers}" -- "${COMP_WORDS[COMP_CWORD]}"))
}

# Completion pour tet-vm
complete -F _tet_vm_enter_completion tet-vm
