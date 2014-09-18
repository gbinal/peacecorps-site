from django import forms
from localflavor.us.forms import USPhoneNumberField, USStateField
from localflavor.us.forms import USZipCodeField, USStateSelect


class DonationPaymentForm(forms.Form):
    
    DONOR_TYPE_CHOICES = (
        ('Individual', 'Individual'),
        ('Organization', 'Organization'),
    )

    PAYMENT_TYPE_CHOICES = (
        ('credit-card', 'Credit Card'), 
        ('ach-bank-check', 'ACH Bank Check'),
    )

    DEDICATION_TYPE_CHOICES = (
        ('in-honor', 'In Honor'),
        ('in-memory', 'In Memory')
    )

    ded_yes = "I authorize the Peace Corps to make my name and contact"
    ded_yes += " information available to the honoree."

    ded_no = "I do not authorize the Peace Corps to make my name and contact"
    ded_no += " information available to the honoree."
    
    DEDICATION_CONSENT_CHOICES = (
        ('yes-dedication-consent', ded_yes),
        ('no-dedication-consent', ded_no),
    )


    VOLUNTEER_CONSENT_CHOICES = (
        ('vol-consent-yes', 'Share with Volunteer'), 
        ('vol-consent-no', "Don't share with Volunteer")
    )
    
    donor_type = forms.ChoiceField(
        widget=forms.RadioSelect, choices=DONOR_TYPE_CHOICES,
        initial='Individual')
    name = forms.CharField(label="Name *", max_length=100)
    email = forms.EmailField(required=False)
    street_address = forms.CharField(label="Street Address *", max_length=80)
    city = forms.CharField(label="City *", max_length=40)
    payment_type = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_TYPE_CHOICES, 
        initial="credit-card",
    )
    comments = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.Textarea(attrs={'rows':4}))

    # User consents to stay informed about the Peace Corps. 
    email_consent = forms.BooleanField(initial=True)

    # True if there might be a possible conflict of interest. 
    interest_conflict = forms.BooleanField(initial=False)

    #Dedication related fields
    dedication = forms.BooleanField(initial=False)
    dedication_name = forms.CharField(label="Name", max_length=40)

    dedication_type = forms.ChoiceField(
        widget=forms.RadioSelect, choices=DEDICATION_TYPE_CHOICES,
        initial='in-honor')
    dedication_email = forms.EmailField(label="Email", required=False)
    dedication_address = forms.CharField(
        label="Mailing Address", max_length=255, required=False)
    card_dedication = forms.CharField(max_length=150, required=False)
    dedication_consent = forms.ChoiceField(
        widget=forms.RadioSelect, initial='yes-dedication-consent',
        choices=DEDICATION_CONSENT_CHOICES)
    information_consent = forms.ChoiceField(
        widget=forms.RadioSelect, choices=VOLUNTEER_CONSENT_CHOICES,
        initial='vol-consent-yes')

class USDonationPaymentForm(DonationPaymentForm):
    """ A US address specific donation payment form. Since most of the donors
    will likely reside in the United States, this makes sense. """

    state = USStateField(label="State *", widget=USStateSelect)
    zip_code = USZipCodeField()
    phone_number = USPhoneNumberField(required=False)
