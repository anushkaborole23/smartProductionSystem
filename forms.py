from django import forms
from .models import UserRegistrationModel, AssetLayerModel, UserIntegrationLayerModel, UserCommunicationLayerModel,UserInformationLayerModel,UserFunctionalLayerModel,UserBusinessLayerModel


class UserRegistrationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[a-zA-Z]+'}), required=True, max_length=100)
    loginid = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[a-zA-Z]+'}), required=True, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
                                                                 'title': 'Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters'}),
                               required=True, max_length=100)
    mobile = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[56789][0-9]{9}'}), required=True,
                             max_length=100)
    email = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'}),
                            required=True, max_length=100)
    locality = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 22}), required=True, max_length=250)
    city = forms.CharField(widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'pattern': '[A-Za-z ]+', 'title': 'Enter Characters Only '}), required=True,
        max_length=100)
    state = forms.CharField(widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'pattern': '[A-Za-z ]+', 'title': 'Enter Characters Only '}), required=True,
        max_length=100)
    status = forms.CharField(widget=forms.HiddenInput(), initial='waiting', max_length=100)

    class Meta():
        model = UserRegistrationModel
        fields = '__all__'


class AssetlayerForm(forms.ModelForm):
    unithead = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[a-zA-Z]+'}), required=True, max_length=100)
    productname = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[a-zA-Z]+'}), required=True, max_length=100)
    shift = forms.IntegerField()
    productquantity = forms.IntegerField()
    noofworkers = forms.IntegerField()

    # shift = forms.IntegerField(widget=forms.IntegerField(max_value=3, min_value=1),required=True)
    # productquantity = forms.CharField(widget=forms.IntegerField(), required=True)
    # noofworkers = forms.CharField(widget=forms.IntegerField(), required=True)

    class Meta():
        model = AssetLayerModel
        fields = '__all__'


class UserIntegrationLayerForm(forms.ModelForm):
    engtool = forms.CharField(widget=forms.TextInput(attrs={'pattern': '[a-zA-Z]+'}), required=True, max_length=100)
    filesize = forms.FloatField()
    databasetype = forms.CharField(max_length=100)
    humanmachineinterface = forms.IntegerField()
    plcslaves = forms.IntegerField()

    class Meta():
        model = UserIntegrationLayerModel
        fields = '__all__'


Protocol_CHOICES = (("TCP/IP", "TCP/IP"), ("HTTP", "HTTP"), ("FTP", "FTP"))
Transferred_CHOICES = (("Ethernet", "Ethernet"), ("Bluetooth", "Bluetooth"), ("Wi-Fi", "Wi-Fi"))

class UserCommunicationLayerForm(forms.ModelForm):
    protocol = forms.ChoiceField(choices=Protocol_CHOICES)
    transferred = forms.ChoiceField(choices=Transferred_CHOICES)
    filesize = forms.FloatField()

    class Meta():
        model = UserCommunicationLayerModel
        fields = '__all__'

Storage_CHOICES = (("HDFS", "HDFS"), ("MongoDb", "MongoDb"), ("Kafka", "Kafka"),("MySql","MySql"))
bool_file = (("True","True"),("False","False"))
bool_file2 = (("True","True"),("False","False"))
class UserInformationLayerForm(forms.ModelForm):
    metadata = forms.CharField(max_length=100)
    storagesystems = forms.ChoiceField(choices=Storage_CHOICES)
    schemaregistry = forms.ChoiceField(choices=bool_file)
    da = forms.ChoiceField(choices=bool_file2)
    class Meta():
        model = UserInformationLayerModel
        fields = '__all__'


production_model = (("KafkaStreams","KafkaStreams"),("KubernetCluster","KubernetCluster"))
building_model = (("PySparkMlib","PySparkMlib"),("sparkcluster","sparkcluster"))
os_model = (("Windows","Windows"),("Linux","Linux"),("Mac","Mac"))
class UserFunctionalLayerForm(forms.ModelForm):
    productionmodel = forms.ChoiceField(choices=production_model)
    modelbuilding = forms.ChoiceField(choices=building_model)
    os = forms.ChoiceField(choices=os_model)
    class Meta():
        model = UserFunctionalLayerModel
        fields = '__all__'

class UserBusinessLayerForm(forms.ModelForm):
    anomalyname = forms.CharField(max_length=100)
    energyoptimization = forms.CharField(max_length=100)
    conditionmonitor = forms.CharField(max_length=100)
    class Meta():
        model = UserBusinessLayerModel
        fields = '__all__'
