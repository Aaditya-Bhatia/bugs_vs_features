| Dimension Name | Factors                         | Description                                               |
|----------------|---------------------------------|-----------------------------------------------------------|
| Text           | tf-idf_score_word               | Tf-idf scores of words that are used across all the components of an issue report (Title, body, issue-comments, and answer-comments).|
| QAContent      | ques_pos_body, ques_pos_comment, ques_pos_answer, ques_pos_answerComment | Positive sentiment that is expressed in the body, issue-comments, answers, and answer-comments of the issue report. |
|                | ques_neg_body, ques_neg_comment, ques_neg_answer, ques_neg_answerComment | Negative sentiments expressed in the body, issue-comments, answers, and answer-comments of the issue report. |
|                | ques_neu_body, ques_neu_comment, ques_neu_answer, ques_neu_answerComment | Neutral sentiments expressed in the body, issue-comments, answers, and answer-comments of the issue report. |
|                | ques_comp_body, ques_comp_comment, ques_comp_answer, ques_comp_answerComment | Compound sentiments expressed in the body, issue-comments, answers, and answer-comments of the issue report. |
|                | ques_FRE_body, ques_FRE_comment, ques_FRE_answer, ques_FRE_answerComment | Flesch Readability Ease score of the body, issue-comments, answers, and answer-comments of the issue report. |
|                | ques_words_body, ques_words_comment, ques_words_answer, ques_words_answerComment | Number of words used to describe the body, issue-comments, answers, and answer-comments of an issue report. |
|                | ques_img_body, ques_img_comment, ques_img_answer, ques_img_answerComment | Whether the issue report body/comment/answer/answer comment has inline images, links, code or environment information (i.e., name of the operating system) |
| QAContributions| contrib_ques_edits, contrib_answer_edits | The number of edits performed on issue reports and their answers. |
|                | contrib_ques_answers, contrib_ques_comments, contrib_ans_comments | The number of answers received by the issue report. The number of comments received by the issue report and the answers. |
|                | contrib_upvotes_ques, contrib_downvotes_ques | The number of upvotes and downvotes received by an issue report |
|                | contrib_upvotes_ans, contrib_downvotes_ans | The number of upvotes and downvotes received by the answers |
| QAUser         | user_editors_body, user_answerers, user_commenters, user_answer_commenters | The number of editors, answerers, commenters, and answer-commenters that the issue thread has. |
|                | user_rep_quesAsker, user_rep_quesCommenter, user_rep_ansAsker, user_rep_ansCommenter | Reputation of question askers, question commenters, answer editors, answerers, answer commenters and answer editors. |
