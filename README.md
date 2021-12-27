# Cyber Security Base - Project 1

## LINK: https://github.com/ruusukivi/cyber-security-project1

This Django app is created to demonstrate five mistakes found in OWASP Top Ten list updated 2021. The whole list can be found here https://owasp.org/www-project-top-ten/

App consists of polls, accounts and admin. The set-up is done according tutorials https://docs.djangoproject.com/en/3.2/intro/tutorial01/ and https://github.com/mdn/django-locallibrary-tutorial 

The app is not intended for production use. This is my first Django app.

## FLAW 1 
A04:2021 – Insecure Design 
https://owasp.org/Top10/A04_2021-Insecure_Design/

Insecure design was introduced as a new category in OWASP Top Ten in 2021. It differs from insecure implementation. If the design is insecure, not even a perfect implementation can save it. Insecure design is often related to poor understanding of business risk and use cases. 

In this poll app there was a need to make voting easy in order to get as many votes as possible. Therefore no access control was implemented into voting. It's now very straightforward to vote. However, a user can also vote multiple times. Who cares? What harm could there be? Features like this are useful for trolls and other ill-wishers for opinion distortion and spreading polarization. Do not make this kind of biased voting possible.

### Code link 
https://github.com/ruusukivi/cyber-security-project1/blob/6b1048798960bbc17b7fb8cb941de7bf276ad518/mysite/polls/views.py#L37 

https://github.com/ruusukivi/cyber-security-project1/blob/6b1048798960bbc17b7fb8cb941de7bf276ad518/mysite/polls/templates/polls/detail.html#L8

### How to fix 
Let only authenticated users to vote and allow only one vote per user

### Learn more
One example of poor design is to support credential recovery by questions and answers. This was a common practice some years ago. Many services ask you to provide security questions in order to gain access to your account if you forget your credentials.


## FLAW 2
A07:2021 – Identification and Authentication Failures
https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/

Identification and Authentication Failures include flaws for example in session management, password policy and prevention of automated brute force attacks. 

The polls app lacks all checks to prevent poor passwords. A user can create even a password with only one character.

In addition, the app does not prevent brute force attacks by limiting authentication attempts. Django has in general quite robust authentication, but rate-limit is not a feature that you get out-of-box. 

### Code link
https://github.com/ruusukivi/cyber-security-project1/blob/6b1048798960bbc17b7fb8cb941de7bf276ad518/mysite/accounts/views.py#L8

https://github.com/ruusukivi/cyber-security-project1/blob/6b1048798960bbc17b7fb8cb941de7bf276ad518/mysite/accounts/templates/accounts/signup.html#L10

### How to fix

Add a length requirement for passwords. The longer the better. Passwords should contain uppercase and lowercase letters, numbers and special symbols. Implement weak password checks. OWASP recommends testing new or changed passwords against the top 10,000 worst passwords list. Django has some good validators for passwords https://docs.djangoproject.com/en/4.0/topics/auth/passwords/#module-django.contrib.auth.password_validation 

For rate-limiting at the auth backend level you can use for example https://pypi.org/project/django-ratelimit-backend/ However, the latest release is from Aug 27th in 2018. There might be a a risk of another flaw from OWASP Top Ten List - A06:2021 – Vulnerable and Outdated Components

### Learn more: 
https://sharkbyte.ca/7-common-security-vulnerabilities-to-watch-for-in-your-django-app/


## FLAW 3

A05:2021 – Security Misconfiguration
https://owasp.org/Top10/A05_2021-Security_Misconfiguration/

Security Misconfigurations refer to situations where the system has unnecessary out-dated or otherwise non-secure features enabled or users have more privileges than they need. The system might not have the latest security features enabled or securely configured. Default passwords might be left unchanged.

The app has at least two flaws related to misconfiguration. First, all users are created as superusers. This gives them access to the Django admin with unlimited rights. 

In addition, when users send feedback, the app suggests using their username as their nickname. Nickname is visible for every user. Now the potential attacker needs to figure out only the user's password.

The feedback form is meant only for the logged-in users.  However, the form is only hidden from the index page. You would be able to send feedback by just calling the polls/feedback url with proper values.

### Code link
https://github.com/ruusukivi/cyber-security-project1/blob/6b1048798960bbc17b7fb8cb941de7bf276ad518/mysite/accounts/views.py#L15 

https://github.com/ruusukivi/cyber-security-project1/blob/6b1048798960bbc17b7fb8cb941de7bf276ad518/mysite/polls/templates/polls/index.html#L32

https://github.com/ruusukivi/cyber-security-project1/blob/6b1048798960bbc17b7fb8cb941de7bf276ad518/mysite/polls/templates/polls/index.html#L28

https://github.com/ruusukivi/cyber-security-project1/blob/6b1048798960bbc17b7fb8cb941de7bf276ad518/mysite/polls/views.py#L27


### How to fix

You should have create_user() instead of create_superuser(). Basic users should have their own user group with proper rights. 

The feature suggesting username as a nickname should be removed. Maybe you could ask for a nickname already in sign-up and make sure that a user can select her username as a nickname.

Before the feedback view in views.py you should use @login_required.

### Learn more 
https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/


## FLAW 4 
A03:2021 – Injection
https://owasp.org/Top10/A03_2021-Injection/

Injection includes for example cross-site scripting and SQL injections. If the user-supplied data is not validated, the application is vulnerable to attacks. 

The polls app has a feedback form with xss vulnerability. The product owner wanted to enable bolded text and hyperlinks in feedback messages. Developers solved the need by ignoring validation and adding a safe tag in the feedback message list. Users are now able to bold text and add links, but the app is also vulnerable for attacks. Users can add for example javascript code into the text. There is no validation in the server-side.

### Code link

https://github.com/ruusukivi/cyber-security-project1/blob/6b1048798960bbc17b7fb8cb941de7bf276ad518/mysite/polls/views.py#L27

https://github.com/ruusukivi/cyber-security-project1/blob/6b1048798960bbc17b7fb8cb941de7bf276ad518/mysite/polls/templates/polls/index.html#L20

### How to fix

First, you remove safe tag and add validator in the server-side. Then you either stop supporting bolded text and links or implement a library supporting rich text. Ensuring the user-provided links are safe is tricky. Perhaps you could make a validator that permits only certain domains. Django has many built-in validators to utilize.

### Learn more 
https://docs.djangoproject.com/en/4.0/ref/validators/#built-in-validators 


## FLAW 5
A09:2021 – Security Logging and Monitoring Failures
https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/

Security Logging and Monitoring means for example logging all auditable events like logins, failed logins and transactions. Log messages can be unclear. There can be either too little or too much and irrelevant messages. Without automated alerts many cases can go unnoticed.

In the polls app there is no logging implemented in Settings.

### Code link

https://github.com/ruusukivi/cyber-security-project1/blob/main/mysite/mysite/settings.py

### How to fix

Configuring the Django project's logging system would be the first logical step: https://docs.djangoproject.com/en/4.0/topics/logging/


### Learn more 
https://docs.djangoproject.com/en/4.0/ref/validators/#built-in-validators 

