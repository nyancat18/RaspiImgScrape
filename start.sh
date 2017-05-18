#!/bin/bash
echo "RUN AS ROOT"
systemctl daemon-reload
systemctl enable blogdownloader.service 