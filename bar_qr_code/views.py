
import random
import qrcode
import qrcode.image.svg
from io import BytesIO

from django.shortcuts import render
from django.views.generic import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        template = 'index.html'
        return render(
            request,
            template,
        )


def generate_random_code():
    num = "12345678900987654321"
    numbers = random.sample(num, 5)
    five_last_number = ''
    for number in numbers:
        five_last_number += number

    return five_last_number


class CustomerQrAndBarcodeScan(View):

    def post(self, request, *args, **kwargs):
        templates_text = request.POST['qr_text']
        print(templates_text)
        factory = qrcode.image.svg.SvgImage
        text = generate_random_code()
        print(text)
        img = qrcode.make(text,
                          image_factory=factory, box_size=20)
        streem = BytesIO()
        img.save(streem)
        context = {}
        context['svg'] = streem.getvalue().decode()
        return render(request, "index.html", context)
