#!/bin/sh
mv /etc/resolv.conf /etc/resolv.conf_bkp_dns
echo "#Generated by Pi3CarAudio" >  /etc/resolv.conf
echo "nameserver 8.8.8.8"       >>  /etc/resolv.conf
echo "nameserver 8.8.4.4"       >>  /etc/resolv.conf
