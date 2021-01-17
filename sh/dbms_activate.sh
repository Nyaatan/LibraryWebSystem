#!/bin/bash
set -e
sudo systemctl enable postgresql
sudo systemctl start postgresql
