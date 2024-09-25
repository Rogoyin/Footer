class Partido{
    constructor(local,visitante,golesLocal,golesVisitante,estadio,fecha,arbitro){
        this.local = local;
        this.visitante = visitante;
        this.golesLocal = golesLocal;
        this.golesVisitante = golesVisitante;
        this.estadio = estadio;
        this.fecha = fecha;
        this.arbitro = arbitro;
    }
}

const partido = new Partido("River");

for(let i in partido){
    console.log(i);
}

const locales = ["River Plate", "Boca Juniors", "River Plate", "River Plate", "Boca Juniors"];
const visitantes = ["Boca Juniors", "River Plate", "Boca Juniors", "Boca Juniors", "River Plate"];
const golesLocales = [2,1,3,0,0];
const golesVisitantes = [0,1,1,3,0];
const estadios = ["Monumental", "Bombonera", "Monumental", "Libertadores de América", "Bombonera"];
const fechas = ["02-02-1992", "04-12-1990", "12-05-2015", "13-04-1950", "10-10-2021"];
const arbitro = ["Patricio Lousteau", "Germán Delfino", "Federico Lamolina", "Jorge Castrilli", "Ángel Sánchez"];

const arreglos = [locales,visitantes,golesLocales,golesVisitantes,estadios,fechas,arbitro];
const partidosArray = transponeLista(arreglos);

//Funciones.

//1. Transpone una lista de listas en otra lista de listas.
function transponeLista(listasMadre){
    let listasTranspuestas = []

    //Función nueva.
    listasMadre[0].forEach(function(){
        listasTranspuestas.push([]);
    });

    //Otra.
    listasMadre.forEach(function(lista){
        i = 0;
        while(i<lista.length){
            listasTranspuestas[i].push(lista[i]);
            i++;
        }
    });

    return listasTranspuestas

}


function listaAObjeto(listaDeListas, clase){
    //Transforma una lista de listas en una lista de objetos de la clase que se elige.

    const listaObjetos = [];

    listaDeListas.forEach(function(lista){
        arrayConstructor = [];
        i = 0;
        while (i<lista.lenght){
            arrayConstructor.push(lista[i]);
            i++;
            console.log(arrayConstructor);
        };



    })

}