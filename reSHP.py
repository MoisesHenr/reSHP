from tkinter import *
from tkinter import messagebox
import tkinter.filedialog as fdlg
import sys
from xmlGenerator import *
import shapefile

class reSHP:
	filePath = ""
	boundingBox = [("minX", 1000), ("maxX", -1000), ("minY", 1000), ("maxY", -1000)]

	def __init__(self, toplevel):

		# Janela
		toplevel.title('reSHP')
		#toplevel.iconbitmap('global.ico')
		toplevel.geometry("720x480")

		self.frame1 = Frame(toplevel)
		self.frame1.pack()

		self.frame2 = Frame(toplevel)
		self.frame2.pack()

		self.frame3 = Frame(toplevel)
		self.frame3.pack()

		self.frame4 = Frame(toplevel)
		self.frame4.pack()

		self.frame5 = Frame(toplevel)
		self.frame5.pack()

		self.frame6 = Frame(toplevel)
		self.frame6.pack()

		self.frame7 = Frame(toplevel)
		self.frame7.pack()

		self.frame8 = Frame(toplevel)
		self.frame8.pack()

		self.frame9 = Frame(toplevel)
		self.frame9.pack()

		self.frame10 = Frame(toplevel)
		self.frame10.pack()

		self.frame11 = Frame(toplevel)
		self.frame11.pack()

		##########################################################################

		# Cor e tamanho das letras 
		font1=('Verdana','10')

		self.createMenuBar(toplevel);

		# Spacing 1
		Label(self.frame1,text='', fg='black',
		font=font1, height=1).pack(side=TOP)
		
		# Initial text to information
		Label(self.frame1,text='reSHP: Retângulo Envolvente de arquivos Shapefile', font=font1).pack(side=LEFT)

		# Spacing 2
		Label(self.frame2,text='', fg='black',
		font=font1, height=1).pack(side=TOP)

		# Box 1 directory
		self.directory=Entry(self.frame2,width=50,font=font1)
		self.directory.pack(side=LEFT)
		selectFile=Button(self.frame2, font=font1, text= 'Selecionar arquivo', command=self.selectFile)
		selectFile.pack(side=LEFT)

		# Spacing 3
		Label(self.frame3,text='', fg='black',
		font=font1, height=1).pack(side=TOP)

		# Bounding box calculator
		boundingBoxCalculator=Button(self.frame3, font=font1, text= 'Calcular Retângulo Envolvente', command=self.boundingBoxCalculator)
		boundingBoxCalculator.pack(side=LEFT)

		# Spacing 4
		Label(self.frame4,text='', fg='black',
		font=font1, height=1).pack(side=TOP)

		# Result 
		Label(self.frame4,text='Retângulo Envolvente',width=20,font=font1).pack()

		Label(self.frame5,text='',width=20,font=font1).pack()
		Label(self.frame5,text='Lat. norte',font=font1).pack()
		self.norte=Entry(self.frame5,width=20,font=font1)
		self.norte.pack(side=RIGHT)

		Label(self.frame6,text='Long. oeste',font=font1).pack(side=LEFT)
		self.oeste=Entry(self.frame6,width=20,font=font1)
		self.oeste.pack(side=LEFT)

		Label(self.frame6, width=10, height=4).pack(side=LEFT)

		Label(self.frame6,text='Long. leste',font=font1).pack(side=RIGHT)
		self.leste=Entry(self.frame6,width=20,font=font1)
		self.leste.pack(side=RIGHT)

		Label(self.frame7,text='Lat. sul',font=font1).pack(side=BOTTOM)
		self.sul=Entry(self.frame7,width=20,font=font1)
		self.sul.pack(side=RIGHT)

		# Spacing 5
		Label(self.frame9,text='', fg='black',
		font=font1, height=1).pack(side=TOP)

		# Create XML
		createXML=Button(self.frame9, font=font1, text= 'Salvar XML', command=self.createXML)
		createXML.pack(side=LEFT)

		# Success message
		Label(self.frame10,text='',font=font1).pack(side=TOP)
		self.success = Label(self.frame10,text='',font=font1)
		self.success.pack(side=LEFT)
		
		# copiryght
		Label(self.frame11,text='',font=('Verdana','4')).pack(side=TOP)
		Label(self.frame11,text='Desenvolvido por: Moises H. Pereira',font=('Verdana','6')).pack()
	
	def createMenuBar(self, toplevel):

		menubar = Menu(toplevel)

		options = Menu(menubar, tearoff=0)
		options.add_command(label="Ajuda", command=self.showHelp)
		options.add_command(label="Sobre", command=self.showInfo)
		menubar.add_cascade(label="Opções", menu=options)

		toplevel.config(menu=menubar) 

	def showHelp(self):
		messagebox.showinfo('Passos para utilização do reSHP:', 'Passo 1: clique no botão "Selecionar arquivo" e escolha o arquivo *.shp desejado \nPasso 2: clique no botão "Calcular Retângulo Envolvente" \nPasso 3: se desejar edite os dados gerados para os campos "Lat" e "Long" \nPasso 4: clique no botão "Salvar XML" e escolha o diretório desejado')

	def showInfo(self):
		messagebox.showinfo('Sobre', 'Este programa calcula o retângulo envolvente de arquivos Shapefile, salvando o resultado em um arquivo XML.\nO reSHP foi desenvolvido com o objetivo de facilitar a edição de metadados geoespaciais no editor edpMGB (http://www.dpi.ufv.br/projetos/edpmgb/).\n\nEste programa foi implementado no âmbito de um projeto de Iniciação Científica, financiado pelo CNPq, pelo bolsista Moises Henrique Pereira, sob a orientação do Prof. Jugurta Lisboa Filho, do Departamento de Informática da Universidade Federal de Viçosa (UFV). A primeira versão foi disponibilizada em abril de 2019.')

	def selectFile(self):
		opcoes = {}
		opcoes['defaultextension'] = '.shp'
		opcoes['filetypes'] = [('Shapefile', '.shp'), ('XML', '.xml')]

		self.filePath = fdlg.askopenfilename(**opcoes)
		if self.filePath != "":
			#print(filePath)
			self.directory.delete(0,END)
			self.directory.insert(0,self.filePath)
			self.oeste.delete(0,END)
			self.leste.delete(0,END)
			self.sul.delete(0,END)
			self.norte.delete(0,END)
			self.success['text'] = ''

	def boundingBoxCalculator(self):
		try:
			sf = shapefile.Reader(self.filePath)
			bb = sf.bbox
			print(bb)
			self.boundingBox[0] = ("minX", bb[0])
			self.boundingBox[1] = ("maxX", bb[2])
			self.boundingBox[2] = ("minY", bb[1])
			self.boundingBox[3] = ("maxY", bb[3])

			self.oeste.delete(0,END)
			self.oeste.insert(0,self.boundingBox[0][1])
			self.leste.delete(0,END)
			self.leste.insert(0,self.boundingBox[1][1])
			self.sul.delete(0,END)
			self.sul.insert(0,self.boundingBox[2][1])
			self.norte.delete(0,END)
			self.norte.insert(0,self.boundingBox[3][1])
		except:
			messagebox.showinfo('ERRO!', 'Houve um erro com seu arquivo!')

	def createXML(self):
		fileName = self.filePath.split("/")
		fileName = fileName[-1]
		fileName = fileName[:-4]
		fileName = fileName + "_re.xml";

		self.boundingBox[0] = ("minX", self.oeste.get())
		self.boundingBox[1] = ("maxX", self.leste.get())
		self.boundingBox[2] = ("minY", self.sul.get())
		self.boundingBox[3] = ("maxY", self.norte.get())

		# diretorio de destino
		self.destinyDirectory = fdlg.askdirectory()
		if self.destinyDirectory != "":
			createXML(self.boundingBox, fileName, self.destinyDirectory)
			#verificar existencia do arquivo???
			self.success['text'] = 'Arquivo gerado com sucesso'
	  
app=Tk()
reSHP(app)
app.mainloop()