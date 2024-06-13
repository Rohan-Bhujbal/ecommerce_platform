# Generated by Django 5.0 on 2024-05-10 07:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_rm_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnicomOrderItems',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('uniCode', models.CharField(max_length=256, unique=True)),
                ('unicom_id', models.CharField(blank=True, max_length=256, null=True)),
                ('shippingPackageCode', models.CharField(blank=True, max_length=256, null=True)),
                ('shippingPackageStatus', models.CharField(blank=True, max_length=256, null=True)),
                ('facilityCode', models.CharField(blank=True, max_length=256, null=True)),
                ('facilityName', models.CharField(blank=True, max_length=256, null=True)),
                ('alternateFacilityCode', models.CharField(blank=True, max_length=256, null=True)),
                ('reversePickupCode', models.CharField(blank=True, max_length=256, null=True)),
                ('shippingAddressId', models.IntegerField(blank=True, max_length=256, null=True)),
                ('packetNumber', models.IntegerField(blank=True, max_length=256, null=True)),
                ('type', models.CharField(blank=True, max_length=256, null=True)),
                ('shippingMethodCode', models.CharField(blank=True, max_length=256, null=True)),
                ('itemName', models.CharField(blank=True, max_length=256, null=True)),
                ('itemSku', models.CharField(blank=True, max_length=256, null=True)),
                ('sellerSkuCode', models.CharField(blank=True, max_length=256, null=True)),
                ('channelProductId', models.CharField(blank=True, max_length=256, null=True)),
                ('statusCode', models.CharField(blank=True, max_length=256, null=True)),
                ('code', models.CharField(blank=True, max_length=256, null=True)),
                ('totalPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sellingPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shippingCharges', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shippingMethodCharges', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cashOnDeliveryCharges', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('taxPercentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('onHold', models.BooleanField(default=False)),
                ('cancellationReason', models.CharField(blank=True, max_length=256, null=True)),
                ('color', models.CharField(blank=True, max_length=256, null=True)),
                ('brand', models.CharField(blank=True, max_length=256, null=True)),
                ('size', models.CharField(blank=True, max_length=256, null=True)),
                ('hsnCode', models.CharField(blank=True, max_length=256, null=True)),
                ('totalStateGst', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stateGstPercentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('totalCentralGst', models.DecimalField(decimal_places=2, max_digits=10)),
                ('centralGstPercentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('maxRetailPrice', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sellingPriceWithoutTaxesAndDiscount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shippingChargeTaxPercentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cancellable', models.BooleanField(default=False)),
                ('totalDiscount', models.CharField(blank=True, max_length=256, null=True)),
                ('totalShippingCharges', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'unicom_order_items',
            },
        ),
        migrations.CreateModel(
            name='UnicomOrders',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('uniCode', models.CharField(max_length=256, unique=True)),
                ('displayOrderCode', models.CharField(max_length=256)),
                ('channel', models.CharField(max_length=256)),
                ('displayOrderDateTime', models.DateTimeField(blank=True, max_length=256, null=True)),
                ('status', models.CharField(blank=True, max_length=256, null=True)),
                ('created', models.DateTimeField(blank=True, max_length=256, null=True)),
                ('updated', models.DateTimeField(blank=True, max_length=256, null=True)),
                ('fulfillmentTat', models.DateTimeField(blank=True, max_length=256, null=True)),
                ('customerGSTIN', models.CharField(blank=True, max_length=256, null=True)),
                ('channelProcessingTime', models.DateField(blank=True, max_length=256, null=True)),
                ('priority', models.IntegerField(default=0)),
                ('customerCode', models.CharField(blank=True, max_length=256, null=True)),
                ('bill_name', models.CharField(blank=True, max_length=256, null=True)),
                ('bill_addressLine1', models.CharField(blank=True, max_length=256, null=True)),
                ('bill_addressLine2', models.CharField(blank=True, max_length=256, null=True)),
                ('bill_city', models.CharField(blank=True, max_length=256, null=True)),
                ('bill_district', models.CharField(blank=True, max_length=256, null=True)),
                ('bill_state', models.CharField(blank=True, max_length=256, null=True)),
                ('bill_country', models.CharField(blank=True, max_length=256, null=True)),
                ('bill_pincode', models.CharField(blank=True, max_length=256, null=True)),
                ('bill_phone', models.CharField(blank=True, max_length=256, null=True)),
                ('bill_email', models.EmailField(blank=True, max_length=256, null=True)),
                ('bill_type', models.CharField(blank=True, max_length=256, null=True)),
                ('shipping_addressLine1', models.CharField(blank=True, max_length=256, null=True)),
                ('shipping_addressLine2', models.CharField(blank=True, max_length=256, null=True)),
                ('shipping_city', models.CharField(blank=True, max_length=256, null=True)),
                ('shipping_district', models.CharField(blank=True, max_length=256, null=True)),
                ('shipping_state', models.CharField(blank=True, max_length=256, null=True)),
                ('shipping_country', models.CharField(blank=True, max_length=256, null=True)),
                ('shipping_pincode', models.CharField(blank=True, max_length=256, null=True)),
                ('shipping_phone', models.CharField(blank=True, max_length=256, null=True)),
                ('shipping_email', models.EmailField(blank=True, max_length=256, null=True)),
                ('invoiceCode', models.CharField(max_length=256, null=True)),
                ('invoiceDate', models.DateTimeField(blank=True, max_length=256, null=True)),
                ('code', models.CharField(blank=True, max_length=256, null=True)),
                ('channelShipmentCode', models.CharField(blank=True, max_length=256, null=True)),
                ('saleOrderCode', models.CharField(blank=True, max_length=256, null=True)),
                ('uniStatus', models.CharField(blank=True, max_length=256, null=True)),
                ('shippingPackageType', models.CharField(blank=True, max_length=256, null=True)),
                ('shippingProvider', models.CharField(blank=True, max_length=256, null=True)),
                ('shippingCourier', models.CharField(blank=True, max_length=256, null=True)),
                ('shippingMethod', models.CharField(blank=True, max_length=256, null=True)),
                ('trackingNumber', models.CharField(blank=True, max_length=256, null=True)),
                ('trackingStatus', models.CharField(blank=True, max_length=256, null=True)),
                ('courierStatus', models.CharField(blank=True, max_length=256, null=True)),
                ('podCode', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'unicom_orders',
            },
        ),
    ]
