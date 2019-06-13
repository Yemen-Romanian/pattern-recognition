directory="notMNIST_small"
new_dir="images"
mkdir $new_dir

if [ ! -d "$directory" ]
then

        wget http://yaroslavvb.com/upload/notMNIST/notMNIST_small.tar.gz
        tar -xzf notMNIST_small.tar.gz
        rm notMNIST_small.tar.gz

fi

for letter in "$@"
do
	i=1
	cp -r $directory/$letter $new_dir/
	for file in $new_dir/$letter/*
	do
		mv "$file" "$new_dir/$letter/$i.png"
		i=`expr $i + 1`
	done

done

rm -rf $directory

