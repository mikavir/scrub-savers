# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.


## Code Validation



### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| bag | bag.html | ![screenshot](documentation/validation/w3c/bag-w3c.png) | |
| checkout | checkout.html | ![screenshot](documentation/validation/w3c/checkout-w3c.png) | |
| checkout | checkout_success.html | ![screenshot](documentation/validation/w3c/checkout_success-w3c.png) | |
| contact | contact.html | ![screenshot](documentation/validation/w3c/contact-w3c.png) | |
| contact | success.html | ![screenshot](documentation/validation/w3c/contact-success-w3c.png) | |
| home | index.html | ![screenshot](documentation/validation/w3c/index-w3c.png) | |
| products | add_product.html | ![screenshot](documentation/validation/w3c/add-product-w3c.png) | |
| products | edit_product.html | ![screenshot](documentation/validation/w3c/edit-product-w3c.png) | |
| products | product_detail.html | ![screenshot](documentation/validation/w3c/product-detail-w3c.png) | |
| products | products.html | ![screenshot](documentation/validation/w3c/product-w3c.png) | |
| profiles | profile.html | ![screenshot](documentation/validation/w3c/profile-w3c.png) | |
| reviews | add_review.html | ![screenshot](documentation/validation/w3c/add-review-w3c.png) | |
| reviews | edit_review.html | ![screenshot](documentation/validation/w3c/edit-review-w3c.png) | |
| templates | 404.html | ![screenshot](documentation/validation/w3c/404-w3c.png) | |
| templates | 500.html | ![screenshot](documentation/validation/w3c/500-w3c.png) | |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| checkout | checkout.css | ![screenshot](documentation/validation/jigsaw/checkout-jigsaw.png) | No errors |
| profiles | profile.css | ![screenshot](documentation/validation/jigsaw/profiles-jigsaw.png) | No errors |
| static | base.css | ![screenshot](documentation/validation/jigsaw/base-jigsaw.png) | No errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| checkout | stripe_elements.js | ![screenshot](documentation/validation/jshint/checkout-js-hint.png) | undefined variables from Stripe API |
| profiles | countryfield.js | ![screenshot](documentation/validation/jshint/profiles-js-hint.png) | No errors |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| bag | contexts.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/bag/contexts.py) | ![screenshot](documentation/validation/python/contexts-python.png) | No errors |
| bag | bag_tools.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/bag/templatetags/bag_tools.py) | ![screenshot](documentation/validation/python/bag-tools-python.png) | No errors|
| bag | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/bag/urls.py) | ![screenshot](documentation/validation/python/bag-urls-python.png) | No errors |
| bag | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/bag/views.py) | ![screenshot](documentation/validation/python/bag-views-python.png) | No errors |
| checkout | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/checkout/admin.py) | ![screenshot](documentation/validation/python/checkout-admin-python.png) | No errors |
| checkout | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/checkout/forms.py) | ![screenshot](documentation/validation/python/checkout-forms-python.png) | No errors |
| checkout | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/checkout/models.py) | ![screenshot](documentation/validation/python/checkout-models-python.png) | No errors |
| checkout | signals.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/checkout/signals.py) | ![screenshot](documentation/validation/python/checkout-signals-python.png) | No errors |
| checkout | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/checkout/urls.py) | ![screenshot](documentation/validation/python/checkout-urls-python.png) | No errors |
| checkout | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/checkout/views.py) | ![screenshot](documentation/validation/python/checkout-views-python.png) | No errors |
| checkout | webhook_handler.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/checkout/webhook_handler.py) | ![screenshot](documentation/validation/python/checkout-webhook-handler-python.png) | No errors |
| checkout | webhooks.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/checkout/webhooks.py) | ![screenshot](documentation/validation/python/checkout-webhooks-python.png) | No errors |
| contact | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/contact/forms.py) | ![screenshot](documentation/validation/python/contacts-forms-python.png) | No errors |
| contact | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/contact/urls.py) | ![screenshot](documentation/validation/python/contact-urls-python.png) | No errors |
| contact | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/contact/views.py) | ![screenshot](documentation/validation/python/contact-views-python.png) | No errors |
| home | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/home/urls.py) | ![screenshot](documentation/validation/python/home-urls-python.png) | No errors |
| home | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/home/views.py) | ![screenshot](documentation/validation/python/home-views-python.png) | No errors |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/manage.py) | ![screenshot](documentation/validation/python/manage-python.png) | No errors |
| products | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/products/admin.py) | ![screenshot](documentation/validation/python/products-admin-python.png) | No errors |
| products | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/products/forms.py) | ![screenshot](documentation/validation/python/product-forms-python.png) | No errors |
| products | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/products/models.py) | ![screenshot](documentation/validation/python/products-models-python.png) | No errors |
| products | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/products/urls.py) | ![screenshot](documentation/validation/python/checkout-urls-python.png) | No errors |
| products | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/products/views.py) | ![screenshot](documentation/validation/python/profiles-views-python.png) | No errors |
| products | widgets.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/products/widgets.py) | ![screenshot](documentation/validation/python/product-widgets-python.png) | No errors |
| profiles | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/profiles/admin.py) | ![screenshot](documentation/validation/python/profiles-admin-python.png) | No errors |
| profiles | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/profiles/forms.py) | ![screenshot](documentation/validation/python/profiles-forms-python.png) | No errors |
| profiles | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/profiles/models.py) | ![screenshot](documentation/validation/python/profiles-models-python.png) | No errors |
| profiles | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/profiles/urls.py) | ![screenshot](documentation/validation/python/profiles-urls-python.png) | No errors |
| profiles | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/profiles/views.py) | ![screenshot](documentation/validation/python/profiles-views-python.png) | No errors |
| reviews | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/reviews/admin.py) | ![screenshot](documentation/validation/python/reviews-admin-python.png) | No errors |
| reviews | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/reviews/forms.py) | ![screenshot](documentation/validation/python/reviews-forms-python.png) | No errors |
| reviews | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/reviews/models.py) | ![screenshot](documentation/validation/python/reviews-models-python.png) | No errors |
| reviews | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/reviews/urls.py) | ![screenshot](documentation/validation/python/reviews-urls-python.png) | No errors |
| reviews | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/reviews/views.py) | ![screenshot](documentation/validation/python/reviews-views-python.png) | No errors |
| scrub_savers | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/scrub_savers/settings.py) | ![screenshot](documentation/validation/python/setting-python.png) | No errors |
| scrub_savers | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/scrub_savers/urls.py) | ![screenshot](documentation/validation/python/url-python.png) | No errors |
| scrub_savers | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/scrub-savers/main/scrub_savers/views.py) | ![screenshot](documentation/validation/python/views-python.png) | No errors |

## Browser Compatibility
I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Bag | Checkout | Checkout-success | Contact | 404 |  Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/chrome/chrome-bag.png) | ![screenshot](documentation/browsers/chrome/chrome-checkout-1.png) ![screenshot](documentation/browsers/chrome/chrome-checkout-2.png)| ![screenshot](documentation/browsers/chrome/chrome-checkout-success.png) | ![screenshot](documentation/browsers/chrome/chrome-contact.png) |  ![screenshot](documentation/browsers/chrome/chrome-404.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/firefox/firefox-bag.png) | ![screenshot](documentation/browsers/firefox/firefox-checkout-1.png) ![screenshot](documentation/browsers/firefox/firefox-checkout-2.png)| ![screenshot](documentation/browsers/firefox/firefox-checkout-success.png) | ![screenshot](documentation/browsers/firefox/firefox-contact.png) | ![screenshot](documentation/browsers/firefox/firefox-404.png) | Works as expected |
| Safari | ![screenshot](documentation/browsers/safari/safari-bag.png) | ![screenshot](documentation/browsers/safari/safari-checkout-1.png) ![screenshot](documentation/browsers/safari/safari-checkout-2.png)| ![screenshot](documentation/browsers/safari/safari-checkout-success.png) | ![screenshot](documentation/browsers/safari/safari-contact.png) | ![screenshot](documentation/browsers/safari/safari-404.png) | Works as expected |


| Browser | Contact-success | Home | Add Product | Edit Product | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/chrome/chrome-contact-success.png) | ![screenshot](documentation/browsers/chrome/chrome-home-1.png) ![screenshot](documentation/browsers/chrome/chrome-home-2.png) ![screenshot](documentation/browsers/chrome/chrome-home-3.png) | ![screenshot](documentation/browsers/chrome/chrome-add-product-1.png) ![screenshot](documentation/browsers/chrome/chrome-add-product-2.png)| ![screenshot](documentation/browsers/chrome/chrome-edit-product-1.png) ![screenshot](documentation/browsers/chrome/chrome-edit-product-2.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/firefox/firefox-contact-success.png) | ![screenshot](documentation/browsers/firefox/firefox-home-1.png) ![screenshot](documentation/browsers/firefox/firefox-home-2.png) ![screenshot](documentation/browsers/firefox/firefox-home-3.png)| ![screenshot](documentation/browsers/firefox/firefox-add-product-1.png) ![screenshot](documentation/browsers/firefox/firefox-add-product-2.png) | ![screenshot](documentation/browsers/firefox/firefox-edit-product-1.png) ![screenshot](documentation/browsers/firefox/firefox-edit-product-1.png) | Works as expected |
| Safari | ![screenshot](documentation/browsers/safari/safari-contact-success.png) | ![screenshot](documentation/browsers/safari/safari-home-1.png) ![screenshot](documentation/browsers/safari/safari-home-2.png) ![screenshot](documentation/browsers/safari/safari-home-3.png)| ![screenshot](documentation/browsers/safari/safari-add-product.png) ![screenshot](documentation/browsers/safari/safari-add-product-2.png) |![screenshot](documentation/browsers/safari/safari-edit-product.png) ![screenshot](documentation/browsers/safari/safari-edit-product-2.png)  | Works as expected |


| Browser | Product Detail | Products | Profiles | Add Review | Edit Reviews | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/chrome/chrome-product-detail.png) | ![screenshot](documentation/browsers/chrome/chrome-products.png) | ![screenshot](documentation/browsers/chrome/chrome-profile.png) | ![screenshot](documentation/browsers/chrome/chrome-add-review.png) | ![screenshot](documentation/browsers/chrome/chrome-edit-review.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/firefox/firefox-product-detail.png) | ![screenshot](documentation/browsers/firefox/firefox-products.png) | ![screenshot](documentation/browsers/firefox/firefox-profile.png) | ![screenshot](documentation/browsers/firefox/firefox-add-review.png) | ![screenshot](documentation/browsers/firefox/firefox-edit-review.png) | Works as expected |
| Safari | ![screenshot](documentation/browsers/safari/safari-product-detail.png) | ![screenshot](documentation/browsers/safari/safari-products.png) | ![screenshot](documentation/browsers/safari/safari-profiles.png) | ![screenshot](documentation/browsers/safari/safari-add-review.png) |  ![screenshot](documentation/browsers/safari/safari-edit-review.png) | Works as expected |


## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Bag | Checkout | Checkout-success | Contact | 404 |  Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) 320px | ![screenshot](documentation/responsiveness/mobile/mobile-bag.png) | ![screenshot](documentation/responsiveness/mobile/mobile-checkout.png) | ![screenshot](documentation/responsiveness/mobile/mobile-checkout-fix.png) ![screenshot](documentation/responsiveness/mobile/mobile-checkout-success.png)| ![screenshot](documentation/responsiveness/mobile/mobile-contact.png)|![screenshot](documentation/responsiveness/mobile/mobile-404.png) | Order Number is spilling out of the container. Fix: make order number font smaller |
| Tablet (DevTools) 768px | ![screenshot](documentation/responsiveness/tablet/tablet-bag.png) | ![screenshot](documentation/responsiveness/tablet/tablet-checkout.png) | ![screenshot](documentation/responsiveness/tablet/tablet-checkout-success.png) | ![screenshot](documentation/responsiveness/tablet/tablet-contact.png) | ![screenshot](documentation/responsiveness/tablet/tablet-404.png) | Works as expected |
| Desktop | ![screenshot](documentation/browsers/firefox/firefox-bag.png) | ![screenshot](documentation/browsers/firefox/firefox-checkout-1.png) ![screenshot](documentation/browsers/firefox/firefox-checkout-2.png)| ![screenshot](documentation/browsers/firefox/firefox-checkout-success.png) | ![screenshot](documentation/browsers/firefox/firefox-contact.png) | ![screenshot](documentation/browsers/firefox/firefox-404.png) | Works as expected |
| iPhone 13 Pro(personal mobile) | ![screenshot](documentation/responsiveness/iphone13/iphone-bag.PNG) | ![screenshot](documentation/responsiveness/iphone13/iphone-checkout-1.PNG) ![screenshot](documentation/responsiveness/iphone13/iphone-checkout-2.PNG) ![screenshot](documentation/responsiveness/iphone13/iphone-checkout-3.PNG) | ![screenshot](documentation/responsiveness/iphone13/iphone-checkout-success-1.PNG) ![screenshot](documentation/responsiveness/iphone13/iphone-checkout-success-2.PNG)| ![screenshot](documentation/responsiveness/iphone13/iphone-contact.PNG) ![screenshot](documentation/responsiveness/iphone13/iphone-contact-2.PNG) | ![screenshot](documentation/responsiveness/iphone13/iphone-400.PNG) | Works as expected |

| Device | Product Detail | Products | Profiles | Add Review | Edit Reviews | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) 320px | ![screenshot](documentation/responsiveness/mobile/mobile-product-detail.png) | ![screenshot](documentation/responsiveness/mobile/mobile-products.png) | ![screenshot](documentation/responsiveness/mobile/mobile-profile.png) | ![screenshot](documentation/responsiveness/mobile/mobile-add-review.png) | ![screenshot](documentation/responsiveness/mobile/mobile-edit-review.png) | Works as expected |
| Tablet (DevTools) 768px | ![screenshot](documentation/responsiveness/tablet/tablet-product-detail.png) | ![screenshot](documentation/responsiveness/tablet/tablet-products.png) | ![screenshot](documentation/responsiveness/tablet/tablet-profile.png) | ![screenshot](documentation/responsiveness/tablet/tablet-add-review.png) | ![screenshot](documentation/responsiveness/tablet/tablet-edit-review.png) | Works as expected |
| Desktop | ![screenshot](documentation/browsers/firefox/firefox-product-detail.png) | ![screenshot](documentation/browsers/firefox/firefox-products.png) | ![screenshot](documentation/browsers/firefox/firefox-profile.png) | ![screenshot](documentation/browsers/firefox/firefox-add-review.png) | ![screenshot](documentation/browsers/firefox/firefox-edit-review.png) | Works as expected |
| iPhone 13 Pro(personal mobile) | ![screenshot](documentation/responsiveness/iphone13/iphone-product-detail-1.PNG) ![screenshot](documentation/responsiveness/iphone13/iphone-product-detail-2.PNG)  | ![screenshot](documentation/responsiveness/iphone13/iphone-products.PNG)  | ![screenshot](documentation/responsiveness/iphone13/iphone-profile.PNG) | ![screenshot](documentation/responsiveness/iphone13/iphone-add-review.PNG) ![screenshot](documentation/responsiveness/iphone13/iphone-add-review-2.PNG)| ![screenshot](documentation/responsiveness/iphone13/iphone-edit-review-1.PNG) ![screenshot](documentation/responsiveness/iphone13/iphone-edit-review-2.PNG)|Works as expected |

| Device | Contact-success | Home | Add Product | Edit Product | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) 320px | ![screenshot](documentation/responsiveness/mobile/mobile-contact-success.png) | ![screenshot](documentation/responsiveness/mobile/mobile-home.png) | ![screenshot](documentation/responsiveness/mobile/mobile-add-product.png) | ![screenshot](documentation/responsiveness/mobile/mobile-edit-product.png) | Works as expected |
| Tablet (DevTools) 768px | ![screenshot](documentation/responsiveness/tablet/tablet-contact-success.png) | ![screenshot](documentation/responsiveness/tablet/tablet-home.png) | ![screenshot](documentation/responsiveness/tablet/tablet-add-product.png) | ![screenshot](documentation/responsiveness/tablet/tablet-edit-product.png) | Works as expected |
| Desktop | ![screenshot](documentation/browsers/firefox/firefox-contact-success.png) | ![screenshot](documentation/browsers/firefox/firefox-home-1.png) ![screenshot](documentation/browsers/firefox/firefox-home-2.png) ![screenshot](documentation/browsers/firefox/firefox-home-3.png)| ![screenshot](documentation/browsers/firefox/firefox-add-product-1.png) ![screenshot](documentation/browsers/firefox/firefox-add-product-2.png) | ![screenshot](documentation/browsers/firefox/firefox-edit-product-1.png) ![screenshot](documentation/browsers/firefox/firefox-edit-product-1.png) | Works as expected |
| iPhone 13 Pro (personal mobile) | ![screenshot](documentation/responsiveness/iphone13/iphone-contact-success.PNG) | ![screenshot](documentation/responsiveness/iphone13/iphone-home-1.PNG) ![screenshot](documentation/responsiveness/iphone13/iphone-home-2.PNG) ![screenshot](documentation/responsiveness/iphone13/iphone-home-3.PNG) | ![screenshot](documentation/responsiveness/iphone13/iphone-add-product.PNG) ![screenshot](documentation/responsiveness/iphone13/iphone-add-product-2.PNG)| ![screenshot](documentation/responsiveness/iphone13/iphone-edit-product-1.PNG) ![screenshot](documentation/responsiveness/iphone13/iphone-edit-product-2.PNG)| Works as expected |


## Lighthouse Audit
I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.



| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| bag |![screenshot](documentation/lighthouse/mobile/mobile-bag.png) | ![screenshot](documentation/lighthouse/desktop/desktop-bag.png) | mobile: Improvements to be made to serve images in a next gen format: unable to change this as cloudinary render the images.|
| checkout | ![screenshot](documentation/lighthouse/mobile/mobile-checkout.png) | ![screenshot](documentation/lighthouse/desktop/desktop-checkout.png) | mobile: Affected performance due to render blocking sources such as bootstrap CDN, FontAwesome and Stripe API, Unable to remove these as important for the project's frontend|
| checkout success |  ![screenshot](documentation/lighthouse/mobile/mobile-checkout-success.png) | ![screenshot](documentation/lighthouse/desktop/desktop-checkout-sucess.png) | mobile: Affected performance due to render blocking sources such as bootstrap CDN, FontAwesome and Stripe API, Unable to remove these as important for the project's frontend|
| contact |  ![screenshot](documentation/lighthouse/mobile/mobile-contact.png) |  ![screenshot](documentation/lighthouse/desktop/desktop-contact.png) |  No major warnings |
| contact success| ![screenshot](documentation/lighthouse/mobile/mobile-contact-success.png) |  ![screenshot](documentation/lighthouse/desktop/desktop-contact-success.png) | No major warnings|
| home | ![screenshot](documentation/lighthouse/mobile/mobile-home.png) | ![screenshot](documentation/lighthouse/desktop/desktop-home.png)| mobile: Affected performance due to render blocking sources such as bootstrap CDN, FontAwesome and Stripe API, Unable to remove these as important for the project's frontend |
| Add Product Page| ![screenshot](documentation/lighthouse/mobile/mobile-add-product.png) | ![screenshot](documentation/lighthouse/desktop/desktop-add-product.png) | |
| Edit Product | ![screenshot](documentation/lighthouse/mobile/mobile-edit-product.png) | ![screenshot](documentation/lighthouse/desktop/desktop-edit-product.png) | Affected accessibility due to not having labels with crispy forms |
| Product Detail | ![screenshot](documentation/lighthouse/mobile/mobile-product-detail.png) | ![screenshot](documentation/lighthouse/desktop/desktop-product-detail.png) | Accessbility to be imr=proved due to no labels to forms |
| products | ![screenshot](documentation/lighthouse/mobile/mobile-products.png) | ![screenshot](documentation/lighthouse/desktop/desktop-products.png) | Accessbility due to select |
| profiles | ![screenshot](documentation/lighthouse/mobile/mobile-profile.png) | ![screenshot](documentation/lighthouse/desktop/desktop-profile.png) | No major warnings|
| Add review | ![screenshot](documentation/lighthouse/mobile/mobile-add-review.png) | ![screenshot](documentation/lighthouse/desktop/desktop-add-review.png) | No major warning |
| Edit Review | ![screenshot](documentation/lighthouse/mobile/mobile-edit-review.png)| ![screenshot](documentation/lighthouse/desktop/desktop-edit-review.png) | No major warnings |


## Defensive Programming
Defensive programming was manually tested with the below user acceptance testing:
### Restricted page and Admin Authentication

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Profile | | | | | |
| | Logged out users are not able to access profile and should be redirected to sign in page | Tested the feature by doing brute-forcing the url to profile | The feature behaved as expected| Test concluded and passed | ![gif](documentation/defensive-programming/user-cant%20brute-force-profile.gif) |
| Checkout-success | | | | | |
| | Logged out user should no be able to access other users checkout-success | Tested the feature by brute-forcing the url as a logged out person | The feature was able to access the checkout-success | Test concluded and failed. Will fix | ![gif](documentation/defensive-programming/log-out-user-cant-access-checkout-success.gif) |
| Add Product | | | | | |
| | Logged out user should not be able to access the add product page and will be redirected to a sign in page| Tested the feature by brute-forcing the url| The feature behaved as expected | Test concluded and passed | ![gif](documentation/defensive-programming/logged-out-user-cant-access-add-product.gif) |
| | Standard users are unable to access the add product page and will encounter a message error | Tested the feature by brute forcing the url signed in as a standard user | The feature behaved as expected | Test Concluded and Passed | ![gif](documentation/defensive-programming/standard-users-can't-access-admin.gif) |
| Edit Product | | | | | |
| | Logged out user should not be able to access the add product page and will be redirected to a sign in page |  Tested the feature by brute-forcing the url| The feature behaved as expected| Test concluded and passed | ![gif](documentation/defensive-programming/loggedout-user-can't-access-edit.gif) |
| | Standard users are unable to access the add product page and will encounter a message error  | Tested the feature by brute forcing the url signed in as a standard user | The feature behaved as expected | Test Concluded and Passed | ![gif](documentation/defensive-programming/standard-users-cant-access-edit.gif) |
| Add Review | | | | | |
| | Logged out user should not be able to access the add review page and will be redirected to a sign in page |  Tested the feature by brute-forcing the url| The feature behaved as expected| Test concluded and passed | ![gif](documentation/defensive-programming/loggedout-user-can't-access-add-review.gif) |
| | Users that have not bought the product is unable to add a review and will be lead to an error message | Tested the feature by brute forcing the url signed in as a unverified buyer | The feature behaved as expected | Test Concluded and Passed | ![gif](documentation/defensive-programming/unverified-buyers-can't-access-add-review.gif) |
| Edit Review | | | | | |
| | Logged out user should not be able to access the edit review page and will be redirected to a sign in page |  Tested the feature by brute-forcing the url| The feature behaved as expected| Test concluded and passed | ![gif](documentation/defensive-programming/loggedout-user-can't-access-edit-review.gif) |
| | Users that have not made the review is unable to edit other review and will be lead to an error message | Tested the feature by brute forcing the url signed in as a unverified buyer | The feature behaved as expected | Test Concluded and Passed | ![gif](documentation/defensive-programming/unverified-buyer-unable-to-edit-other-review.gif) |

### CRUD functionality
| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Add Product | | | | | |
| | Admin can add product | Tested the feature by finishing the form and adding a product as an admin | The feature behaved as expected| Test concluded and passed | ![screenshot](documentation/defensive-programming/admin-can-add-product.gif) |
| Edit Product | | | | | |
| | Admin can edit product | Tested the feature by finishing the form and editing a product as an admin| The feature behaved as expected| Test concluded and passed | ![screenshot](documentation/defensive-programming/admin-can-edit-product.gif) |
| Delete Product | | | | | |
| | Admin can delete product | Tested the feature by clicking delete and proceeding to confirm deletion with a modal | The feature behaved as expected| Test concluded and passed | ![screenshot](documentation/defensive-programming/admin-can-delete-product.gif) |
| Add Review | | | | | |
| | Verified buyer can add a review | Tested the feature by finishing the form and adding a review as a verified buyer | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/defensive-programming/verified-buyer-can-add-review.gif) |
| Edit Review | | | | | |
| | Verified buyer can edit their own review | Tested the feature by finishing the form and editing a review as a verified buyer and reviewer | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/defensive-programming/verified-buyer-can-edit-review.gif) |
| Delete Review | | | | | |
| | Verified buyer can delete their own review | Tested the feature and deleting the review | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/defensive-programming/verified-buyer-can-delete-own-review.gif) |
| Profile | | | | | |
| | User can update their personal details | Tested the feature by updating the form  | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/defensive-programming/user-can-update-profile.gif) |

### Form validation
The form validation is handled by Django Crispy Forms:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Add product | | | | | |
| | Form is expected to not submit and display a error message if one required field is unmet | Tested the feature by doing submitting the form without price | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/defensive-programming/add-product-form-validation.gif) |
| Edit Product | | | | | |
| | Form is expected to not submit and display a error message if one required field is unmet | Tested the feature by doing submitting the form without price | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/defensive-programming/edit-product-form-validation.gif) |
| Add Review | | | | | |
| | Form is expected to not submit and display a error message if one required field is unmet | Tested the feature by doing submitting the form without rating | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/defensive-programming/add-review-form-validation.gif) |
| Contact | | | | | |
| | Form is expected to not submit and display a error message if one required field is unmet | Tested the feature by doing submitting the form without valid email and without a message| The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/defensive-programming/contact-form-validation.gif) |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a Shopper, I want to be able to view a list of products so that I can select items to purchase. | ![screenshot](documentation/features/feature06.png) |
| As a Shopper, I want to be able to view individual product details so that I can identify the price, description, and product details. | ![screenshot](documentation/features/feature23.png) |
| As a Shopper, I want to easily view the total of my purchases at any time so that I can avoid overspending. | ![screenshot](documentation/features/feature17.png) |
| As a Shopper, I want to easily register for an account so that I can have a personal account to view my purchase history. | ![screenshot](documentation/features/feature13.png) |
| As a Shopper, I want to easily log in to my account so that I can keep track of my purchase history.| ![screenshot](documentation/features/feature12.png) |
| As a Shopper, I want to easily log out of my account so that my account is secure when using a public device. | ![screenshot](documentation/features/feature11.png) |
| As a Shopper, I want to have a personalized user profile so that I can view my purchase history, order confirmations, and save my payment history. | ![screenshot](documentation/features/feature08.png) |
| As a Shopper, I want to sort the list of available products so that I can easily identify the best-rated, best-priced, and categorically sorted products. | ![screenshot](documentation/features/feature06.png) |
|  As a Shopper, I want to search for a product by name or description so that I can find the specific product I want to purchase. | ![screenshot](documentation/features/feature07.png) |
| As a Shopper, I want to easily select the size and quantity of a product when purchasing it so that I don't accidentally select the wrong size. |![screenshot](documentation/features/feature24.png)  |
|  As a Shopper, I want to view an order confirmation after checkout so that I can verify that I haven't made any mistakes. | ![screenshot](documentation/features/feature25.png)|
|  As a Shopper, I want to adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout. | ![screenshot](documentation/features/feature27.png)|
|  As a Shopper, I want to receive an email confirmation after my purchase so that I have a record of my purchase. | ![screenshot](documentation/features/feature26.PNG)| |
|  As a Store Owner, I want to add a product so that I can add new items to my store. | ![screenshot](documentation/features/feature20.png)| |
|  As a Store Owner, I want to edit a product so that I can change the product information easily. | ![screenshot](documentation/features/feature21.png) |
|  As a Store Owner, I want to delete a product so that I can remove items that are no longer for sale. |  ![screenshot](documentation/features/feature21.png)|
|  As a Store Owner, I want to have a logo so that I can improve my brand identity.| ![screenshot](documentation/features/feature28.png) |
|  As a Shopper, I want to see contact information so that I can feel safe knowing that I can contact someone to remedy any mistakes.| ![screenshot](documentation/features/feature05.png) |
|  As a Shopper, I want to see reviews so that I can understand the quality of the product I'm buying.| ![screenshot](documentation/features/feature15.png) |
|  As a Store Owner, I want to be contacted so that I can improve customer loyalty and understand if there are improvements to be made.|![screenshot](documentation/features/feature14.png)|

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

`pip3 install coverage`

`pip3 freeze --local > requirements.txt`

`coverage run --omit=*/site-packages/*,*/migrations/*,*/__init__.py,env.py manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File |  Screenshot |
| --- | --- |  --- |
| Bag | tests.py |  ![screenshot](documentation/test/test-bag.png) |
| Home | tests.py |  ![screenshot](documentation/test/test-home.png) |
| Products | tests.py |  ![screenshot](documentation/test/test-products.png) |
| Contact | tests.py | ![screenshot](documentation/test/test-contact.png) |


#### Unit Test Issues

To test the "Add Product" views, I first needed to create a superuser. The test script automatically handles this by creating a superuser and logging them in.
```python
# https://stackoverflow.com/questions/33274874/assertionerror-302-200
        # Log superuserin
        self.client = Client()
        user = User.objects.create_superuser('test_admin', password)
        self.client.force_login(user=user)
```
When testing the views for the reviews section, I faced challenges in simulating a logged-in user who both purchases a product and submits a review. This process was similar to testing the checkout section, where a bag of products is required to proceed.
## Bugs

## Fixed bugs
- Internal sever error due to sample being negative.

    ![screenshot](documentation/bugs/bug-1.png)

    - The original code in the home views attempts to render 4 randomly recommended items, but this causes an error when there are fewer than 4 products available.
    
    - *original code:*
    `products = random.sample(products, 4)`
   - To fix this, I added a condition to only sample the products if there are more than 4 available:
    *fixed code*
    ```python
        if len(products) > 4:
        products = random.sample(products, 4)
    ```

- Anonymous user is not iterable
    ![screenshot](documentation/bugs/bug-2.png)

    - When an unsigned user attempts to make a purchase, they encounter an internal server error (500) during the checkout success process. This error occurs because the code tries to iterate through an AnonymousUser, which does not have an associated profile.

    To resolve this, I added a condition to check if the user is signed in before attempting to retrieve their profile.

    ```python
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()
    ```
- Static files was not being collected to staticfiles with deployment.
    ![screenshot](documentation/bugs/bug-3.png)

    -After configuring Whitenoise to serve static files, we were unable to collect them into the staticfiles directory. Manually copying static files into the directory didn't resolve the issue, as it failed to include static files from other apps. As a result, critical files like stripe.js were missing, which prevented payments from working during checkout.

    The issue was caused by the incorrect order of apps in the INSTALLED_APPS setting—specifically, `django.contrib.staticfiles` was placed below `Cloudinary`. To fix this, I reordered the apps, ensuring `django.contrib.staticfiles` is listed above `Cloudinary`.
    ```python
    INSTALLED_APPS = [
        '...',
        'django.contrib.staticfiles',
        'cloudinary_storage',
        'cloudinary',
    ]
    ```
- The delete modal was deleting the wrong product. For example, when clicking the delete button for the product "Crocs," the modal incorrectly pointed to "Trousers" instead. After debugging, I discovered that the issue was caused by the product IDs not being unique in the modal, leading to mismatches between the clicked item and the product shown in the modal.

    ![screenshot](documentation/bugs/bug-4.png)

To resolve this, I ensured that each product ID was made unique.

- Empty Rating Causes Database Error: When a user submits the form to add a review without selecting a rating, it results in a database error due to the None value being submitted. This issue arose because the form validation was not triggered effectively, as the rating field was not generated using Crispy Forms.

    ![screenshot](documentation/bugs/bug-4.png)

To resolve this issue, I implemented validation for the rating field in forms.py by adding a custom validation method within the ProductReviewForm class:
```python
        def clean_rating(self):
            rating = self.cleaned_data.get('rating')
            if not rating:
                raise forms.ValidationError("Please select a rating.")
            return rating
```
I have also implemented additional defensive programming to ensure the form is only submitted if the rating is valid. The updated code checks both the form's validity and whether a rating has been selected:

```python
    rating = request.POST.get('rating')
    if form.is_valid() and rating:  # Check if the form is valid and rating is selected
```

## Unfixed Bugs
- User can bruteforce an URL of another user's checkout-success/ order confirmation if they know the URL. 

    ![gif](documentation/defensive-programming/log-out-user-cant-access-checkout-success.gif)

- I have been exploring solutions to prevent this issue, but they would involve restricting unsigned users from purchasing products. This is a known vulnerability, as noted in the Code Institute's Boutique Ado walkthrough. Additionally, the links are highly unique, making it unlikely that users would remember the exact URL.