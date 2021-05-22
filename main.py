# from tags.TagsClass import TagClass
# print(TagClass("Done again").show_name())

# from tags import TagsClass
# tc = TagsClass.TagClass("Done")
# print(tc.show_name())

# from tags import tags
# tags.show_tags()

# from tags.tags import show_tags
# show_tags()

from movies import Movie

mo = Movie.Movie

#print(next(mo.load("./data/movies.dat")))

for m in mo.load_all("./data/movies.dat"):
    print(m.name)


