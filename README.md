# Cyber Security Base - Project 1

This app is created to demostrate five mistakes found in OWASP Top Ten list updated 2021. The whole list can be found here https://owasp.org/www-project-top-ten/

App consists of polls, accounts, feedback and admin. The set-up is done according tutorials https://docs.djangoproject.com/en/4.0/intro/tutorial01/ and https://github.com/mdn/django-locallibrary-tutorial The app is not intended for production use. This is my first Django app.

Repository link: https://github.com/ruusukivi/cyber-security-project1

## FLAW 1: A04:2021 – Insecure Design 
https://owasp.org/Top10/A04_2021-Insecure_Design/

Insecure design was introduced as a new category in OWASP Top Ten in 2021. It differs from insecure implementation. If the design is insecure, not even a perfect implementation can save it. Insecure design is often related to poor understanding of business risk and use cases. 

In this poll app there was a need to make voting easy in order to get as many votes as possible. Therefore no access control was implemented into voting. It's now very straightforward to vote. However, a user can also vote multiple times. Who cares? What harm there could be? Features like this are useful for trolls and other ill-wishers for opinion distortion and spreading polarization. Do not make this kind of biased voting possible.

### Code link 

### How to fix 
Let only authenticated users to vote and allow only one vote per user

### Learn more
One example of poor design is to support credential recovery by questions and answers. This was a common practice some years ago. Many services asked you to provide security questions in order to gain access to your account if you forget your credentials.


## FLAW 2: A07:2021 – Identification and Authentication Failures
https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/

Identification and Authentication Failures include flaws for example in session management, password policy and prevention of automated brute force attacks. 

The poll app lacks all checks to prevent poor passwords. A user can create even a password with only one character.

In addition, the app does not prevent brute force attacks by limiting authentication attemps. Django has in general quite robust authentication, but rate-limit is not a feature that you get out-of-box. 

### Code link

### How to fix

Add a length requirement for passwords. The longer the better. Passwords should contain uppercase and lowercase letters, numbers and special symbols. Implement weak password checks. OWASP recommends testing new or changed passwords against the top 10,000 worst passwords list.

For rate-limiting at the auth backend level you can use for example https://pypi.org/project/django-ratelimit-backend/ However, the latest release is from Aug 27th in 2018. There might be a a risk of another flaw from OWASP Top Ten List - A06:2021 – Vulnerable and Outdated Components

### Learn more: 
https://sharkbyte.ca/7-common-security-vulnerabilities-to-watch-for-in-your-django-app/)


## FLAW 3: A05:2021 – Security Misconfiguration
https://owasp.org/Top10/A05_2021-Security_Misconfiguration/

Security Misconfigurations refer to situations where the system has unnecessary out-dated or otherwise unsecure features enabled or users have more priviledges than they need. The system might not have the latest security features enabled or securily configured. Default passwords might be left unchanged.

The app has at least two flaws related to misconfiguration. First, all users are created as superusers. This gives them access to the Django admin with unlimited rights. 

In addition, when users send feedback, the app suggests to use their username as their nickname. Nickname is visible for every user. Now the potential attacker needs to figure out only user's password.

The feedback form is meant only for the logged in users.  However, the form is only hidden from the index page. You would be able to send feedback by just calling the polls/feedback url with proper values.

### Code link

### How to fix

You should have create_user() instead of create_superuser(). Basic users should have their own user group with proper rigths. 

Feature suggesting username as a nickname should be removed. Maybe you could ask nickname already in sign up and make sure that a user can select her username as a nickname.

Before feedback view in views.py you should use @login_required.



