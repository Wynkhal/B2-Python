#! C:\Users\Valentin\AppData\Local\Programs\Python\Python36-32\python.exe
# 3a-save
# script d'archivage
# 11/10/2018
# RAFFY Valentin

# import des divers modules
import signal
import shutil
import gzip
import os
import sys

# fonction anti ctrlC


def ctrlC(sig, frame):
    deleteBackup()
    sys.exit(0)


signal.signal(signal.SIGINT, ctrlC)


# Fonction qui mets en place un Backup


def makeBackup():
    os.remove(data_path + '/backup.tar.gz')
    shutil.move(backup + '.tar.gz', data_path)

# Fontion qui supprime la Backup déjà existante


def deleteBackup():
    if os.path.exists(backup + '.tar.gz'):
        os.remove(backup + '.tar.gz')


# Variables
data_path = os.path.expanduser('~/data/')
directory_path = os.path.expanduser('~/B2-Python/scripts')
backup = os.path.expanduser('~/backup')
disk_capacity = os.system("df -h | grep '%s'")


try:
    os.makedirs(data_path, exist_ok=True)
except OSError:
    if not os.path.isdir(data_path):
        os.system("mkdir data_path")


for partition in ['/home', '/var']:
    sys.stdout.write(
        "Espace libre de la partition " + partition + " : " +
        str(disk_capacity) + "G\n")

if disk_capacity > 3:
    if os.access(data_path, os.W_OK and os.R_OK):

        # On crée un backup
        shutil.make_archive(backup, 'gztar', directory_path)

        # On regarde si un ancien backup existe
        if os.path.exists(data_path + '/backup.tar.gz'):

            # On va lire à l'interieur de la backup existante
            with gzip.open(data_path + '/backup.tar.gz', 'rb') as f:
                exist_save = f.read()
            # On va lire la nouvelle backup
            with gzip.open(backup + '.tar.gz', 'rb') as f:
                new_save = f.read()

            # On compare les deux
            if exist_save != new_save:
                # On remplace l'ancienne par la nouvel
                makeBackup()
                sys.stdout.write('Succes : La sauvegarde a été effectuer\n')
            # On gère toute les erreurs possible
            else:
                deleteBackup()
                sys.stdout.write('Erreur : La sauvegarde existe déjà\n')

        else:
            shutil.move(backup + '.tar.gz', data_path)
            sys.stdout.write('Succes : La sauvegarde a été effectuer\n')

    else:
        sys.stderr.write('Erreur : Vous n\'avez pas les droits nécessaire\n')

else:
    sys.stderr.write('Il n\'y a pas assez d\'espace libre sur la partition')