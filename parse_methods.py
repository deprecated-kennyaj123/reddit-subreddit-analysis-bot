# This file contains only methods that are run once, and do not run over time

import praw
import bot_helpers


def average_top_comment_length(subreddit, time='week', min_comment_score=1, min_submission_score=1):
    """Checks all the submissions and returns the length of the top comments
    :param subreddit: the subreddit to be scraped
    :param time: can be "week" or "day" - Gathers submissions from the last day or week
    :param min_comment_score: only process comments above this score threshold
    :param min_submission_score:  min_submission_upvotes: only process submissions above this score threshold
    :returns: int of average top comment length

    Run time: 1089 seconds (18 minutes, 9 seconds) w/ default params on /r/cars
    """

    the_submissions = []

    if time == 'week':
        for submission in subreddit.get_top_from_week(limit=None):
            if submission.score >= min_submission_score:
                the_submissions.append(submission)
    elif time == 'day':
        for submission in subreddit.get_top_from_day(limit=None):
            if submission.score >= min_submission_score:
                the_submissions.append(submission)
    else:
        return 'Not a valid :param time: - must be either "day" or "week"'

    parent_comments = []
    for submission in the_submissions:
        for comment in submission.comments:
            if isinstance(comment, praw.objects.Comment) \
                    and comment.score >= min_comment_score:
                parent_comments.append(comment)

    comment_lengths = []
    for comment in parent_comments:
        comment_lengths.append(len(comment.body))

    average_length = sum(comment_lengths)/len(comment_lengths)
    return int(average_length)


def comment_keyword_count_parser(subreddit, keywords, time='week', min_comment_score=1, min_submission_score=1):
    """Returns how many times each keyword appears in the comments of the posts in the last day or week
    Run time: 783 seconds (13 minutes, 8 seconds) w/ default params on /r/cars """
    the_submissions = []
    the_count = []

    if time == 'week':
        for submission in subreddit.get_top_from_week(limit=None):
            if submission.score >= min_submission_score:
                the_submissions.append(submission)
            else:
                break
    elif time == 'day':
        for submission in subreddit.get_top_from_day(limit=None):
            if submission.score >= min_submission_score:
                the_submissions.append(submission)
            else:
                break
    else:
        return 'Not a valid :param time: - must be either "day" or "week"'

    the_comments = []
    for submission02 in the_submissions:
        for comment in praw.helpers.flatten_tree(submission02.comments):
            if isinstance(comment, praw.objects.Comment) \
                    and comment.score >= min_comment_score:
                the_comments.append(comment)

    for keyword in keywords:
        the_count.append(bot_helpers.keyword_count(keyword, the_comments))

    tuple_result = []
    for keyword, a_count in zip(keywords, the_count):
        tuple_result.append((keyword, a_count))
    return tuple_result


def self_vs_linked_ratio(subreddit, time='week', min_score=1):
    """Returns the ratio of self posts to linked posts in the subreddit over the last day or week

    :param time: Either day or week, determines what submissions to retrieve
    :param min_score: minimum score a submission must have to be considered

    Run time: 14 seconds w/ default params on /r/cars"""

    submissions = []

    if time == 'week':
        for submission in subreddit.get_top_from_week(limit=None):
            if submission.score >= min_score:
                submissions.append(submission)
    elif time == 'day':
        for submission in subreddit.get_top_from_day(limit=None):
            if submission.score >= min_score:
                submissions.append(submission)
    else:
        return 'Not a valid :param time: - must be either "day" or "week"'

    self_count = 0
    link_count = 0
    total_count = len(submissions)
    ratio = -1

    for submission in submissions:
        if submission.is_self:
            self_count += 1
        else:
            link_count += 1
    ratio = bot_helpers.simplify_ratio(self_count, link_count)

    return self_count, link_count, ratio
