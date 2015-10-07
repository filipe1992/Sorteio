__author__ = 'Filipe Damasceno'

import wx, random #importando as bibliotecas.

class Interface(wx.Frame):#criando a class
    def __init__(self, parent=None, id=-1, titulo ="sorteio"): #constructor
        wx.Frame.__init__(self,parent,id,titulo,size=(420,480)) #constructor da super classe
        self.scroll = wx.ScrolledWindow(self,-1) #cria um painel com scroll
        self.tc = wx.StaticText(self.scroll,-1,label="NOME DO VENCEDOR: ",pos=(120,10)) #cria um texto estatico
        self.saida = wx.TextCtrl(self.scroll,-1,value="seu numero PODE aparecer aqui!!!",size=(200, 50),pos=(80,30),style=wx.PORT_MSW | wx.VSCROLL | wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_CHARWRAP) #cria uma janela dinamica
        self.saida.SetBackgroundColour(wx.WHITE) #cores
        self.saida.SetForegroundColour(wx.BLACK)
        self.butao = wx.Button(self.scroll,wx.ID_OK,"agora vai..",pos=(140,100)) #cria um botao
        self.imag = wx.Image("camisa-branca.png",wx.BITMAP_TYPE_ANY).Scale(300,300) #le a imagem
        self.imagem =wx.StaticBitmap(self.scroll, wx.ID_ANY, wx.BitmapFromImage(self.imag),pos=(50,140))salva a imagem
        self.butao.Bind(wx.EVT_BUTTON,self.noEnviar) evento no botao

    def noEnviar(self,event): #o evento em si
        self.saida.Clear() limpa a saida
        self.saida.SetValue((int(random.random()*46)+1).__str__()) #escreve na janela

app =wx.App()
frame = Interface()
frame.Show()
app.MainLoop()
