import numpy as np
import re 

with open("entrada.txt", "r") as entrada:
	lines = [line.split() for line in entrada]

i = (len(lines))
j = 0
Var = []
while j < i:
	if j == 0:
		m = 1
	else:
		m = 0
	var = []
	while m < len(lines[j]):
		v = re.search('[a-zA-Z][\d]', lines[j][m])
		v2 = re.search('[a-zA-Z]', lines[j][m])
		if v:
			var.insert(m, lines[j][m])
		elif v2:
			var.insert(m, lines[j][m])
		m += 1
	Var.insert(j, var)
	var = []
	j += 1
 
print(Var)	

j = 0
k = 0
m = 0
count = 1


j = 0
ld = []
le = []
obj = []
while j < i:
	m = 1
	aux = len(lines[j]) - 1
	d = []
	e = []
	if j == 0:
	# parenteses resolvido
		f = ''
		a = 0
		b = 0
		while m < len(lines[j]):
			p1 = re.search('[(]', lines[j][m])
			if p1:
				a = m + 1
				b = m + 1
			m += 1
		while a < len(lines[j]):
			if lines[j][a] != ')':
				f += lines[j][a]
				lines[j][a] = ''
			else:
				lines[j][a] = ''
				break
			a += 1
		lines[j][b-1] = f
		m = 1 
	# negativos resolvido
		while m < len(lines[j]) - 1:
			if lines[j][m] == '-':
				lines[j][m+1] = "-" + lines[j][m+1]
			m += 1
		m = 1
	# sinais/espaço em branco resolvido
		while m < len(lines[j]):
			if lines[j][m] == '-' or lines[j][m] == '+' or lines[j][m] == '':
				m += 1
			else:
				obj.insert(m, lines[j][m])
				m += 1
		m = 0
	# letras resolvido
		while m < len(obj):
			p = re.search('[a-zA-Z][\d]', obj[m])
			p2 = re.search('[a-zA-Z]', obj[m])
			if p:
				obj[m] = re.sub('[a-zA-Z][\d]', '1', obj[m])
			if p2:
				obj[m] = re.sub('[a-zA-Z]', '1', obj[m])
			m += 1
	# * resolvido
		m = 0
		while m < len(obj):
			op = re.search('[*]', obj[m])
			if op:
				del obj[m+1]
				del obj[m]
			m += 1
	# / resolvido
		m = 0
		while m < len(obj):
			op = re.search('[/]', obj[m])
			if op:
				r = 0
				r2 = 0
				g = ''
				h = ''
				while r < len(obj[m]):
					if obj[m][r] != '/':
						g += obj[m][r]
						r += 1
					else:
						break
				r += 1
				while r < len(obj[m]):
					h += obj[m][r]
					r += 1
				n = int(g)/int(h)
				obj[m] = n
			m += 1
	if j > 0:
		L = []
		while m < len(lines[j]):
			op = re.search('[<=>]', lines[j][m])
			if op:
				aux = m
			m += 1
		m = 0
		if lines[j][aux] == '>=':
			while m < len(lines[j]):
				mais = re.search('[+]', lines[j][m])
				menos = re.search('[-]', lines[j][m])
				p1 = re.search('[a-zA-Z][\d]', lines[j][m])
				p2 = re.search('[\d]', lines[j][m])
				if mais:
					lines[j][m] = "-"
				if menos:
					lines[j][m] = "+"
				if (p1 and m == 0) or (p2 and m == (aux + 1) and lines[j][m] != '0'):
						lines[j][m] = "-" + lines[j][m]
				m += 1
			lines[j][aux] = '<='
		# if lines[j][aux] == '==':
	# parenteses resolvido
		f = ''
		a = 0
		b = 0
		while m < len(lines[j]):
			p1 = re.search('[(]', lines[j][m])
			if p1:
				a = m + 1
				b = m + 1
			m += 1
		while a < len(lines[j]) and a > 0:
			if lines[j][a] != ')':
				f += lines[j][a]
				lines[j][a] = ''
			else:
				lines[j][a] = ''
				break
			a += 1
		if (b - 1) >= 0:
			lines[j][b-1] = f
		m = 0
	# negativos resolvido
		while m < len(lines[j]) - 1:
			if lines[j][m] == '-':
				lines[j][m+1] = "-" + lines[j][m+1]
			m += 1
		m = 0
	# sinais/espaço em branco resolvido
		while m < (len(lines[j]) ):
			if lines[j][m] == '-' or lines[j][m] == '+' or lines[j][m] == '':
				m += 1
			else:
				L.insert(m, lines[j][m])
				m += 1
	# * resolvido
		m = 0
		while m < len(L):
			op = re.search('[*]', L[m])
			if op:
				L[m-1] += L[m+1]
				del L[m+1]
				del L[m]
			m += 1
		m = 0
		while m < len(L):
			op = re.search('[<]', L[m])
			if op:
				aux = m
			m += 1
		m = 0
		while m < len(L):
			p1 = re.search('[a-zA-Z][\d]', L[m])
			p2 = re.search('[a-zA-Z]', L[m])
			p3 = re.search('[\d]', L[m])
			if m < aux and (p1 or p2):
				e.insert(m, L[m])
			elif m < aux and p3:
				if L[m][0] != '-':
					s = "-" + L[m]
					d.insert(m, s)
				else:
					s = L[m]
					s = re.sub('[-]', '', s)
					d.insert(m, s)
			elif m > aux and (p1 or p2):
				if L[m][0] != '-':
					s = "-" + L[m]
					e.insert(m, s)
				else:
					s = L[m]
					s = re.sub('[-]', '', s)
					e.insert(m, s)
			elif m > aux and p3:
				d.insert(m, L[m])
			m += 1
		ld.insert(j-1, d)
		le.insert(j-1, e)
	# / resolvido
		m = 0
		while m < len(le[j-1]):
			op = re.search('[/]', le[j-1][m])
			if op:
				p = re.search('[a-zA-Z][\d]', le[j-1][m])
				p2 = re.search('[a-zA-Z]', le[j-1][m])
				if p:
					le[j-1][m] = re.sub('[a-zA-Z][\d]', '', le[j-1][m])
				if p2:
					le[j-1][m] = re.sub('[a-zA-Z]', '', le[j-1][m])
			m += 1
		m = 0
		while m < len(le[j-1]):
			op = re.search('[/]', le[j-1][m])
			if op:
				r = 0
				g = ''
				h = ''
				while r < len(le[j-1][m]):
					if le[j-1][m][r] != '/':
						g += le[j-1][m][r]
						r += 1
					else:
						break
				r += 1
				while r < len(le[j-1][m]):
					h += le[j-1][m][r]
					r += 1
				n = str(int(g)/int(h))
				le[j-1][m] = n
			m += 1
		m = 0
	# letras resolvido
		while m < len(le[j-1]):
			p = re.search('[a-zA-Z][\d]', le[j-1][m])
			p2 = re.search('[a-zA-Z]', le[j-1][m])
			if p:
				le[j-1][m] = re.sub('[a-zA-Z][\d]', '1', le[j-1][m])
			if p2:
				le[j-1][m] = re.sub('[a-zA-Z]', '1', le[j-1][m])
			m += 1
	# variáveis livres
	j += 1

# Obj = []
# Obj.append([float(i) for i in obj])
# Ax = np.array((i-1, len(le)), dtype=float)
# Ax = np.array(le)
# b = np.array((i-1, len(ld)), dtype=float)
# b = np.array(ld)
# print(Obj)
# print(Ax)
# print(b)

t = 0
j = 1
while j < i:
	maior = t
	if len(lines[j]) > t:
		t = maior
	j += 1

# Ax = np.zeros(((t-2), (i-2)))
# Ax = np.array(le)