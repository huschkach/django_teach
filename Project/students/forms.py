import datetime

from django import forms
import re


class NameForm(forms.Form):
    your_name = forms.CharField(label="Dein Name:", max_length=120)


class StudentForm(forms.Form):
    firstname = forms.CharField(label="Vorname", max_length=128)
    lastname = forms.CharField(label="Nachname", max_length=128)
    birthday = forms.CharField(label="Geburtstag")
    studentID = forms.IntegerField(label="StudentID", min_value=0)
    phone = forms.CharField(label="Telefonnummer", max_length=20,
                            required=False)

    def clean_birthday(self):
        pattern = (r"^((\d{4}-\d{2}-\d{2})|(\d{2}\.\d{2}\.\d{4}))( \d{2}:\d{"
                   r"2}:\d{2})?$")
        birthday_str = self.cleaned_data['birthday']

        dt_birthday = datetime.datetime.now()

        if re.search(pattern, birthday_str) is not None:
            pattern1 = r"^\d{4}-\d{2}-\d{2}$"
            pattern2 = r"^\d{4}-\d{2}-\d{2} \d{1,2}:\d{2}:\d{2}$"
            pattern3 = r"^\d{2}\.\d{2}\.\d{4}$"
            pattern4 = r"^\d{2}\.\d{2}\.\d{4} \d{1,2}:\d{2}:\d{2}$"

            if re.search(pattern1, birthday_str):
                try:
                    dt_birthday = datetime.datetime.strptime(birthday_str,
                                                             "%Y-%m-%d")
                except Exception as ex:
                    raise forms.ValidationError
            elif re.search(pattern2, birthday_str):
                try:
                    dt_birthday = datetime.datetime.strptime(birthday_str,
                                                             "%Y-%m-%d "
                                                             "%H:%M:%S")
                except Exception as ex:
                    raise forms.ValidationError
            elif re.search(pattern3, birthday_str):
                try:
                    dt_birthday = datetime.datetime.strptime(birthday_str,
                                                             "%d.%m.%Y")
                except Exception as ex:
                    raise forms.ValidationError
            elif re.search(pattern4, birthday_str):
                try:
                    dt_birthday = datetime.datetime.strptime(birthday_str,
                                                             "%d.%m.%Y "
                                                             "%H:%M:%S")
                except Exception as ex:
                    raise forms.ValidationError

            dt_now = datetime.datetime.now()

            if 18 <= (dt_now.year - dt_birthday.year) < 70:
                print("Zu alt/Zu jung")
                raise forms.ValidationError

            return dt_birthday

        raise forms.ValidationError





