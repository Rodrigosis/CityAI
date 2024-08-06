class CharacterTraits:

    def __init__(self, foo: int = 100) -> None:
        self.foo = foo
    
    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "foo": self.foo
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            foo=data["foo"]
        )


"""
Líder Nato:

Confiante, autoritário e motivador.
Gosta de tomar decisões e guiar os outros.
Foca em alcançar objetivos e metas.
Introvertido Pensador:

Reflexivo, analítico e reservado.
Prefere passar tempo sozinho ou com poucas pessoas.
Interessado em atividades intelectuais.
Aventureiro Espontâneo:

Impulsivo, entusiasta e curioso.
Gosta de explorar novos lugares e experimentar coisas novas.
Vive no momento e busca emoções.
Protetor Leal:

Devotado, confiável e altruísta.
Prioriza o bem-estar dos amigos e da família.
Está sempre pronto para ajudar e defender os outros.
Artista Sonhador:

Criativo, sensível e introspectivo.
Se expressa através da arte, música ou escrita.
Tem uma visão única e um forte senso de estética.
Empreendedor Ambicioso:

Determinado, competitivo e inovador.
Busca sucesso e reconhecimento profissional.
Está sempre em busca de novas oportunidades de negócios.
Realista Prático:

Lógico, pragmático e confiável.
Prefere soluções práticas e realistas.
Valoriza a estabilidade e a segurança.
Idealista Humanitário:

Comprometido, empático e visionário.
Luta por justiça social e causas humanitárias.
Quer fazer do mundo um lugar melhor.
Comediante Alegre:

Divertido, extrovertido e espirituoso.
Adora fazer os outros rirem e se divertir.
Leva a vida de forma leve e otimista.
Estudioso Perfeccionista:

Meticuloso, detalhista e disciplinado.
Busca excelência em tudo que faz.
Tem uma forte ética de trabalho e dedicação aos estudos.
Acolhedor Sociável:

Amigável, carismático e generoso.
Gosta de socializar e conhecer novas pessoas.
Cria um ambiente acolhedor ao seu redor.
Estrategista Calculista:

Racional, metódico e reservado.
Planeja cuidadosamente seus passos.
Tem uma mente lógica e analítica.
Explorador Solitário:

Independente, aventureiro e introspectivo.
Prefere a solidão e busca autoconhecimento.
Gosta de viajar e explorar por conta própria.
Diplomata Pacífico:

Paciente, comunicativo e mediador.
Busca harmonia e evita conflitos.
Tem habilidades de negociação e diplomacia.
Romântico Idealista:

Sonhador, apaixonado e sensível.
Valoriza o amor e os relacionamentos.
Tem uma visão romântica da vida.
Inventor Criativo:

Inovador, curioso e engenhoso.
Gosta de criar novas coisas e resolver problemas.
Tem uma mente cheia de ideias.
Filósofo Reflexivo:

Pensador profundo, curioso e introspectivo.
Busca entender o sentido da vida e das coisas.
Gosta de debates filosóficos e teóricos.
Aventureiro Destemido:

Corajoso, impulsivo e enérgico.
Gosta de desafios e esportes radicais.
Vive para aventuras e novas experiências.
Empático Cuidador:

Carinhoso, sensível e protetor.
Coloca as necessidades dos outros antes das suas.
Trabalha em profissões que envolvem cuidar dos outros.
Tecnólogo Nerd:

Apaixonado por tecnologia, curioso e estudioso.
Adora gadgets, programação e jogos.
Passa muito tempo no mundo digital.
"""
