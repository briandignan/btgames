from fabric.api import run, sudo, local, cd, env
from fabric.operations import put, get, prompt
from fabric.contrib.files import exists, append
from fabric.context_managers import settings
from fabric.api import env
import time
import os

def install():
    """Installs your bittorrent client on a fresh Ubuntu 12.04"""
    sudo('apt-get update')
    sudo('apt-get install -y python-pip python-dev build-essential git')
    run('mkdir tulva') 
    with cd('tulva'):
    	run('wget http://jari.takkala.net/files/tulva')

def torrentfile(torrentfile):
    """What to do with the local torrent file"""
    #This version copies the torrent file to the ubuntu home directy
    put(os.path.basename(torrentfile), 'test.torrent')

def download():
    """Code to download """
    # after the torrent file
    with cd('tulva'):
        run('time tulva ../test.torrent 2>&1 >tulva.log')
