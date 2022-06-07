#Iterate over  tuples
def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        # concatenating with singleton tuple
        nums = nums + (t[0],)
        # only add words haven't added before
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

test = ((1,"a"),(2,"b"),(1,"a"),(7,"b"))
(a, b, c) = get_data(test)
print("a:", a,"b:",b,"c:",c)


# apply to actual data
tswift = ((2014, "Katy"),
            (2014, "Harry"),
            (2012, "Jake"),
            (2010, "Taylor"),
            (2008, "Joe"))

(min_year, max_year, num_people)= get_data(tswift)
print("From ", min_year, " to ",max_year, " Taylor Swift wrote songs about ",num_people)