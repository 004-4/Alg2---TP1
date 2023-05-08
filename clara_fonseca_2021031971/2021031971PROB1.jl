
using JuMP
using HiGHS

mutable struct Info
    n::Int #numero de vertices
	plimite::Int #peso máximo das caixas
	caixa::Array{Int} #lista com as caixas
end

function readData(file)
	n = 0
    plimite = 0
    caixa = []
	for l in eachline(file)
		q = split(l, " ")
		if q[1] == "n"
			n = parse(Int64, q[2])
		elseif q[1] == "l"
			plimite = parse(Int64, q[2])
		elseif q[1] == "o"
			push!(caixa, parse(Int64, q[3]))
		end
	end
	return Info(n, plimite, caixa)
end

function Imprimindo(data, x, c)
	for j = 1: data.n
        if(value(c[j]) >= 0.5)
            for i = 1: data.n
                if(value(x[i,j]) >= 0.5)
			        print(i)
			        print(" ")
                end
            end
            println()
		end
	end
end

function Imprimindo2(saida, data, x, sol)
    write(saida,"$sol\n")
	for j = 1: data.n
        if(value(c[j]) >= 0.5)
            for i = 1: data.n
                if(value(x[i,j]) >= 0.5)
					write(saida,"$i ")
                end
            end
			write(saida,"\n")
		end
	end
end

model = Model(HiGHS.Optimizer)

file = open(ARGS[1], "r")

data = readData(file)

@variable(model, x[i=1:data.n, j=1:data.n], Bin) #x[i,j] = 1 caso objeto i esteja na caixa de nº j
@variable(model, c[i=1:data.n], Bin) #c[1] = 1 se a caixa 1 estiver sendo usada

for i = 1:data.n
    @constraint(model, sum(x[i,j] for j in data.n) == 1) #garante que pelo menos uma caixa tenha pelo menos um objeto dentro
end

for j = 1:data.n
	@constraint(model, sum(x[i,j] * data.caixa[i] for i in data.n) <= (data.plimite * c[j])) #a soma dos pesos dos objetos em x[i,j] não pode ultrapassar o limite estipulado
end

@objective(model, Min, sum(c[j] for j=1:data.n))

optimize!(model)

sol = objective_value(model)

saida = open(ARGS[2], "w")

Imprimindo2(saida, data, x, sol)
Imprimindo(data,x,c)