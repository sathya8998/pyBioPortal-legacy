# Commands Git BASH inside repository folder

# version definition
VERSION="v1.0.0"

# move to main directory
cd ..

git pull origin master
git archive --format=tar -o ./archive/pybioportal-"$VERSION".tar.gz setup.py LICENSE.txt README.md
git add .
git commit -m "Create new archive $VERSION"
git push origin master