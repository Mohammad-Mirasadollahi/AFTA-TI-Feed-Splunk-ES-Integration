#!/bin/bash

# Variables
SERVICE_PATH="/etc/systemd/system/afta.service"
SCRIPT_PATH="/root/scripts/afta.py"
TIMER_PATH="/etc/systemd/system/afta.timer"

# Create the service file
echo "[Unit]
Description=afta Python Script Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 $SCRIPT_PATH
User=root
Restart=on-failure
RestartSec=30s
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target" > $SERVICE_PATH

# Create the timer file
echo "[Unit]
Description=Run afta Python Script Service every 24 hours

[Timer]
OnBootSec=5min
OnUnitActiveSec=24h

[Install]
WantedBy=timers.target" > $TIMER_PATH

# Reload the systemd daemon, enable and start the service and timer
systemctl daemon-reload
systemctl enable afta.service
systemctl enable afta.timer
systemctl start afta.timer

echo "Service and timer created and started successfully."
