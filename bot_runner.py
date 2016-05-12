import praw
import time
import bot_helpers
import parse_methods

if __name__ == "__main__":

    start_time = time.time()

    subreddit_name = 'cars'
    red = praw.Reddit('User Auth') # figure out legitimate user authentication string
    the_subreddit = red.get_subreddit(subreddit_name)

    keywords = bot_helpers.get_keywords_from_stupid_txt_file('carManufacturers.txt')

    # parse_methods.comment_keyword_count_parser(the_subreddit, keywords)
    # parse_methods.self_vs_linked_ratio(the_subreddit
    # parse_methods.average_top_comment_length(the_subreddit)

    print(parse_methods.average_top_comment_length(the_subreddit))
    print("--- %s seconds ---" % (time.time() - start_time))