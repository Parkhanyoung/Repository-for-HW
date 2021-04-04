import csv


def module(movie_list_box):
    blank = []
    for each_movie in movie_list_box:
        title = each_movie.find("dt", {"class": "tit"}).find("a").text
        img = each_movie.find("div", {"class": "thumb"}).find("img")['src']
        score = each_movie.find("div", {"class": "star_t1"}).find(
            "span", {"class": "num"}).text
        opendate0 = each_movie.find(
            "dl", {"class": "info_txt1"}).find_all("dd")[0].text
        opendate = opendate0.replace('\r', '').replace(
            '\t', '').replace('\n', '').split("|")[-1].replace(" 개봉", "")
        direct0 = each_movie.find(
            "dl", {"class": "info_txt1"}).find_all("dd")[1].text
        direct = direct0.replace('\r', '').replace('\t', '').replace('\n', '')
        actor0 = each_movie.find(
            "dl", {"class": "info_txt1"}).find_all("dd")[-1].text
        actor = actor0.replace('\r', '').replace('\n', '').replace('\t', '')
        movie_info = {
            "title": title,
            "img": img,
            "score": score,
            "direct": direct,
            "actor": actor,
            "opendate": opendate
        }
        blank.append(movie_info)
    return blank
