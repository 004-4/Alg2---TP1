mutable struct Info
    n::Int #numero de períodos
	c::Array{FLoat} #custo por período
	d::Array{Float} #demanda por período
    s::Array{Float} #estoque por período
    p::Array{Float} #multa por período
end

function readData(file)
	n = 0
    c = []
    d = []
    s = []
    p = []

	for l in eachline(file)
		q = split(l, " ")
		if q[1] == "n"
			n = parse(Int64, q[2])
		elseif q[1] == "c"
			push!(c, parse(FLoat32, q[2]))
		elseif q[1] == "d"
			push!(d, parse(FLoat32, q[2]))
        elseif q[1] == "s"
			push!(s, parse(FLoat32, q[2]))
        elseif q[1] == "p"
			push!(p, parse(FLoat32, q[2]))
		end
	end
	return Info(n, c, d, s, p)
end

model = Model(HiGHS.Optimizer)

file = open(ARGS[1], "r")

data = readData(file)

@variable(model, x[i=1:data.n, j=1:data.n], Bin) #x[i,j] = 1 se o produto i é entregue no período j

for i in data.n
    @constraint(model, sum(x[i,j] * data[j].p  * data[j].d for j in data.n) + sum(x[i,j] * data[j+1].c * data[j].d for j in data.n) < sum(x[i,j] * data[j].c * data[j].d for j in data.n)) 
    @constraint(model, sum(x[i,j] * data[j].s  * data[j+1].d for j in data.n) + sum(x[i,j] * data[j].c * data[j+1].d for j in data.n) < sum(x[i,j] * data[j+1].c * data[j+1].d for j in data.n))
end
for j in data.n
    @objective(model, Min, sum(x[i,j] * data[j].c * data[j].d) + sum(x[i,j] * data[j].s * data[j].d) + sum(x[i,j] * data[j].p * data[j].d))
end

optimize!(model)

sol = objective_value(model)

saida = open(ARGS[2], "w")
Imprimindo(saida, data, x)
