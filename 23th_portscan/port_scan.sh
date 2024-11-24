#!/bin/bash

# Function to check and activate firewall
function check_firewall {
    if ! ufw status >/dev/null 2>&1; then
        sudo ufw enable
        echo "Firewall activated successfully."
    else
        echo "Firewall is already active."
    fi
}

# Function to print open ports in the specified format
function print_open_ports {
    sudo ufw status numbered | grep "ALLOW" | awk '{print $2}' | while read port; do
        direction="i"
        if sudo ufw status numbered | grep "$port" | grep "OUT" >/dev/null 2>&1; then
            direction="o"
        elif sudo ufw status numbered | grep "$port" | grep "IN" >/dev/null 2>&1 && sudo ufw status numbered | grep "$port" | grep "OUT" >/dev/null 2>&1; then
            direction="i"
        fi
        printf "%s %s " "$port" "$direction"
    done
    echo
}

# Function to check a specific port status
function check_port_status {
    read -p "Enter port number: " port
    if sudo ufw status numbered | grep "$port" >/dev/null 2>&1; then
        echo "Port $port is open."
    else
        echo "Port $port is closed."
    fi
}

# Function to close ports except for a given list
function close_other_ports {
    read -p "Enter ports to keep open (format: 443,80i,555o): " ports
    sudo ufw deny proto tcp from any to any port ! "$ports"
}

# Function to create a firewall backup
function create_backup {
    sudo ufw status verbose > ufw_backup.txt
    echo "Firewall backup created successfully."
}

# Function to restore a firewall backup
function restore_backup {
    if [ -f ufw_backup.txt ]; then
        sudo ufw restore < ufw_backup.txt
        echo "Firewall restored successfully."
    else
        echo "Backup file not found."
    fi
}

# Function to export a list of open ports
function export_open_ports {
    sudo ufw status numbered | grep "ALLOW" | awk '{print $2}' > open_ports.txt
    echo "Open ports exported to open_ports.txt"
}

# Function to print port status using netstat
function print_port_status_netstat {
    read -p "Enter port number: " port
    netstat -tulpn | grep "$port" | awk '{print $4}'
}

# Function to inactive firewall
function inactive_firewall {
    sudo ufw disable
    echo "Firewall deactivated successfully."
}

# Main script
check_firewall

while true; do
    echo "What do you want to do?"
    echo "1. Print open ports"
    echo "2. Check a specific port"
    echo "3. Close other ports"
    echo "4. Create firewall backup"
    echo "5. Restore firewall backup"
    echo "6. Export open ports"
    echo "7. Print port status using netstat"
    echo "8. Inactive firewall"
    echo "9. Exit"

    read -p "Enter your choice: " choice

    case $choice in
        1) print_open_ports ;;
        2) check_port_status ;;
        3) close_other_ports ;;
        4) create_backup ;;
        5) restore_backup ;;
        6) export_open_ports ;;
        7) print_port_status_netstat ;;
        8) inactive_firewall ;;
        9) exit 0 ;;
        *) echo "Invalid choice. Please try again." ;;
    esac
done