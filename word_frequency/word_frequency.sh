s=$(cat words.txt |
    gsed 's/ /\n/g'
)
echo "s = $s"


words=(${s})


# echo $words
for word in ${words[@]};
do
    echo "word = $word";
////done

# declare -A words_map
# 
# words_map[one]=1
# words_map[two]=2
# words_map[three]=3
# 
# 
# for key in "${(@k)words_map}";
# do
#     echo $key;
# done
