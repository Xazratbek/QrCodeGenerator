from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

class QrCode(models.Model):
    name = models.CharField(max_length=500)
    qr_code = models.ImageField(upload_to="qr_codes", blank=True,null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        QRcode = qrcode.QRCode()
        QRcode.add_data(self.name)
        QRcode.make()
        QRimg = QRcode.make_image(
            image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(),color_mask=RadialGradiantColorMask(),
            )
        name = f"qr-code-{str(self.id)}.png"
        buffer = BytesIO()
        QRimg.save(buffer, 'PNG')
        self.qr_code.save(name, File(buffer), save=False)
        QRimg.close()
        super().save(*args, **kwargs)