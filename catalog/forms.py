from django import forms

from .models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price"]

    def clean(self):
        cleaned_data = super().clean()
        forbidden_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]

        for field in ["name", "description"]:
            text = cleaned_data.get(field, "").lower()
            for word in forbidden_words:
                if word in text:
                    self.add_error(
                        field,
                        f"Запрещенное слово в {self.fields[field].label}: {word}",
                    )

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ["product", "version_number", "version_name", "is_current"]
