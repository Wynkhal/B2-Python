#! C:\Users\Valentin\AppData\Local\Programs\Python\Python36-32\python.exe
# 3b-opt.py
# Script permettant d'effectuer une sauvegarde sur N repertoires
# Date: 11/11/2018
# Raffy Valentin

# Importations des modules
import signal
import shutil
import gzip
import os
import sys
import subprocess


# Fonction qui cree une archive
def createArchive():
    os.remove(path_data + '/archive.tar.gz')
    shutil.move(archive + '.tar.gz', path_data)


# Fontion qui supprime l'archive déjà existante
def supprArchive():
    if os.path.exists(archive + '.tar.gz'):
        os.remove(archive + '.tar.gz')


# Fonction qui quitte proprement le prog
def end_prog(sig, frame):
    supprArchive()
    sys.exit(0)


# Defini le lien du dossier a sauvegarder
def get_path():
  parser = argparse.ArgumentParser()
  parser.add_argument("-p" ,"--path", help="Lien vers le dossier a archiver")
  args = parser.parse_args()
  if args.path:
    return args.path
  else:
    return '~/B2-Python/scripts'


signal.signal(signal.SIGINT, end_prog)

# Variables
path_data = os.path.expanduser('~/data/')
path_directory = os.path.expanduser(get_path())
archive = os.path.expanduser('~/archive')


# On try pour voir si l'archive existe sinon on la crée
try:
    os.makedirs(path_data, exist_ok=True)
except OSError:
    if not os.path.isdir(path_data):
        raise


# On vérifie la taille dans les partitions /home et /var
for partition in ['/home', '/var']:
    # Recupere en Go
    detail_disk = subprocess.getoutput("df -h | grep '%s'" % partition)

    sys.stdout.write("Espace libre de la partition " + partition + " : " + detail_disk.split()[3] + "\n")

# On vérifie qu'il reste plus de 5 Go de libre
if float(detail_disk.split()[3][:-2].replace(',', '.')) > 5:

    # On regarde si on a les permissions W & R
    if os.access(path_data, os.W_OK and os.R_OK):

        # On crée l'archive
        shutil.make_archive(archive, 'gztar', path_directory)

        # On regarde si une ancienne save existe
        if os.path.exists(path_data + '/archive.tar.gz'):

            # On va lire à l'interieur de la save existante
            with gzip.open(path_data + '/archive.tar.gz', 'rb') as f:
                exist_save = f.read()
            # On va lire la nouvelle save maintenant
            with gzip.open(archive + '.tar.gz', 'rb') as f:
                new_save = f.read()

            # On compare les deux save
            if exist_save != new_save:
                # On supprime l'ancienne et on sauvegarde la nouvelle
                createArchive()
                sys.stdout.write('Succes : La sauvegarde a été effectuer\n')

            else:
                supprArchive()
                sys.stdout.write('Erreur : La sauvegarde existe déjà\n')

        else:
            shutil.move(archive + '.tar.gz', path_data)
            sys.stdout.write('Succes : La sauvegarde a été effectuer\n')

    else:
        sys.stderr.write('Erreur : Vous ne disposez pas des droits sur le répertoire de destination\n')

else:
    sys.stderr.write('Il n\'y a pas assez d\'espace libre sur la partition')