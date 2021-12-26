# Cyber Security Base - Project 1

This app is created to demostrate five mistakes found in OWASP Top Ten list updated 2021. The whole list can be found here https://owasp.org/www-project-top-ten/

App consists of polls, accounts, feedback and admin. The set-up is done according tutorials https://docs.djangoproject.com/en/4.0/intro/tutorial01/ and https://github.com/mdn/django-locallibrary-tutorial The app is not intended for production use. This is my first Django app.

Repository link: https://github.com/ruusukivi/cyber-security-project1

FLAW 1: A04:2021 – Insecure Design 
https://owasp.org/Top10/A04_2021-Insecure_Design/

Insecure design was introduced as a new category in OWASP Top Ten in 2021. It differs from insecure implementation. If the design is insecure, not even a perfect implementation can save it. Insecure design is often related to poor understanding of business risk and use cases. 

In this poll app there was a need to make voting easy in order to get as many votes as possible. Therefore no access control was implemented into voting. It's now very straightforward to vote. However, a user can also vote multiple times. Who cares? What harm there could be? Features like this are useful for trolls and other ill-wishers for opinion distortion and spreading polarization. Do not make this kind of biased voting possible.

How to fix: Let only authenticated users to vote and allow only one vote per user

Learn more: One example of poor design is to support credential recovery by questions and answers. This was a common practice some years ago. Many services asked you to provide security questions in order to gain access to your account if you forget your credentials.

