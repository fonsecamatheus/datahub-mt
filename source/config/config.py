from datetime import datetime

config = [
    {
        'pesquisa': 'Produção Agrícola Municipal (PAM)',
        'tabelas': [
            {
                'id': 5457,
                'nome': 'Área plantada ou destinada à colheita, área colhida, quantidade produzida, rendimento médio e valor da produção das lavouras temporárias e permanentes',
                'variaveis': [
                    {'id': 8331, 'nome': 'Área plantada ou destinada à colheita'},
                    {'id': 216, 'nome': 'Área colhida'},
                    {'id': 214, 'nome': 'Quantidade produzida'}
                ],
                'classificacoes': [
                    {
                        'id': 782,
                        'categorias': [
                            {'id': 40129, 'nome': 'Abacate'},
                            {'id': 40092, 'nome': 'Abacaxi*'},
                            {'id': 45982, 'nome': 'Açaí'},
                            {'id': 40329, 'nome': 'Alfafa fenada'},
                            {'id': 40130, 'nome': 'Algodão arbóreo (em caroço)'},
                            {'id': 40099, 'nome': 'Algodão herbáceo (em caroço)'},
                            {'id': 40100, 'nome': 'Alho'},
                            {'id': 40101, 'nome': 'Amendoim (em casca)'},
                            {'id': 40102, 'nome': 'Arroz (em casca)'},
                            {'id': 40103, 'nome': 'Aveia (em grão)'},
                            {'id': 40131, 'nome': 'Azeitona'},
                            {'id': 40136, 'nome': 'Banana (cacho)'},
                            {'id': 40104, 'nome': 'Batata-doce'},
                            {'id': 40105, 'nome': 'Batata-inglesa'},
                            {'id': 40137, 'nome': 'Borracha (látex coagulado)'},
                            {'id': 40468, 'nome': 'Borracha (látex líquido)'},
                            {'id': 40138, 'nome': 'Cacau (em amêndoa)'},
                            {'id': 40139, 'nome': 'Café (em grão) Total'},
                            {'id': 40140, 'nome': 'Café (em grão) Arábica'},
                            {'id': 40141, 'nome': 'Café (em grão) Canephora'},
                            {'id': 40330, 'nome': 'Caju'},
                            {'id': 40106, 'nome': 'Cana-de-açúcar'},
                            {'id': 40331, 'nome': 'Cana para forragem'},
                            {'id': 40142, 'nome': 'Caqui'},
                            {'id': 40143, 'nome': 'Castanha de caju'},
                            {'id': 40107, 'nome': 'Cebola'},
                            {'id': 40108, 'nome': 'Centeio (em grão)'},
                            {'id': 40109, 'nome': 'Cevada (em grão)'},
                            {'id': 40144, 'nome': 'Chá-da-índia (folha verde)'},
                            {'id': 40145, 'nome': 'Coco-da-baía*'},
                            {'id': 40146, 'nome': 'Dendê (cacho de coco)'},
                            {'id': 40147, 'nome': 'Erva-mate (folha verde)'},
                            {'id': 40110, 'nome': 'Ervilha (em grão)'},
                            {'id': 40111, 'nome': 'Fava (em grão)'},
                            {'id': 40112, 'nome': 'Feijão (em grão)'},
                            {'id': 40148, 'nome': 'Figo'},
                            {'id': 40113, 'nome': 'Fumo (em folha)'},
                            {'id': 40114, 'nome': 'Girassol (em grão)'},
                            {'id': 40149, 'nome': 'Goiaba'},
                            {'id': 40150, 'nome': 'Guaraná (semente)'},
                            {'id': 40115, 'nome': 'Juta (fibra)'},
                            {'id': 40151, 'nome': 'Laranja'},
                            {'id': 40152, 'nome': 'Limão'},
                            {'id': 40116, 'nome': 'Linho (semente)'},
                            {'id': 40260, 'nome': 'Maçã'},
                            {'id': 40117, 'nome': 'Malva (fibra)'},
                            {'id': 40261, 'nome': 'Mamão'},
                            {'id': 40118, 'nome': 'Mamona (baga)'},
                            {'id': 40119, 'nome': 'Mandioca'},
                            {'id': 40262, 'nome': 'Manga'},
                            {'id': 40263, 'nome': 'Maracujá'},
                            {'id': 40264, 'nome': 'Marmelo'},
                            {'id': 40120, 'nome': 'Melancia'},
                            {'id': 40121, 'nome': 'Melão'},
                            {'id': 40122, 'nome': 'Milho (em grão)'},
                            {'id': 40265, 'nome': 'Noz (fruto seco)'},
                            {'id': 40266, 'nome': 'Palmito'},
                            {'id': 40267, 'nome': 'Pera'},
                            {'id': 40268, 'nome': 'Pêssego'},
                            {'id': 40269, 'nome': 'Pimenta-do-reino'},
                            {'id': 40123, 'nome': 'Rami (fibra)'},
                            {'id': 40270, 'nome': 'Sisal ou agave (fibra)'},
                            {'id': 40124, 'nome': 'Soja (em grão)'},
                            {'id': 40125, 'nome': 'Sorgo (em grão)'},
                            {'id': 40271, 'nome': 'Tangerina'},
                            {'id': 40126, 'nome': 'Tomate'},
                            {'id': 40127, 'nome': 'Trigo (em grão)'},
                            {'id': 40272, 'nome': 'Triticale'},
                            {'id': 40153, 'nome': 'Urucum (semente)'},
                            {'id': 40273, 'nome': 'Uva'}
                        ]
                    }
                ],
                'ano_inicio': 1974,
                'ano_fim': datetime.now().year
            }
        ],
    },
    {
        'pesquisa': 'Produção da Extração Vegetal e da Silvicultura (PEVS)',
        'tabelas': [
            {
                'id': 289,
                'nome': 'Quantidade produzida e valor da produção na extração vegetal, por tipo de produto extrativo',
                'variaveis': [
                    {'id': 144, 'nome': 'Quantidade produzida na extração vegetal'},
                    {'id': 145, 'nome': 'Valor da produção na extração vegetal'}
                ],
                'classificacoes': [
                    {
                        'id': 193,
                        'categorias': [
                            {'id': 3403, 'nome': '1.1 - Açaí (fruto)'},
                            {'id': 3404, 'nome': '1.2 - Castanha-de-caju'},
                            {'id': 3405, 'nome': '1.3 - Castanha-do-pará'},
                            {'id': 3406, 'nome': '1.4 - Erva-mate'},
                            {'id': 3407, 'nome': '1.5 - Mangaba (fruto)'},
                            {'id': 3408, 'nome': '1.6 - Palmito'},
                            {'id': 39409, 'nome': '1.7 - Pequi (fruto)'},
                            {'id': 3409, 'nome': '1.8 - Pinhão'},
                            {'id': 3410, 'nome': '1.9 - Umbu (fruto)'},
                            {'id': 3412, 'nome': '2.1 - Ipecacuanha ou poaia (raiz)'},
                            {'id': 3413, 'nome': '2.2 - Jaborandi (folha)'},
                            {'id': 3414, 'nome': '2.3 - Urucum (semente)'},
                            {'id': 3417, 'nome': '3.1 - Caucho'},
                            {'id': 3418, 'nome': '3.2 - Hevea (látex coagulado)'},
                            {'id': 3419, 'nome': '3.3 - Hevea (látex líquido)'},
                            {'id': 40524, 'nome': '3.4 - Mangabeira'},
                            {'id': 3421, 'nome': '4.1 - Carnaúba (cera)'},
                            {'id': 3422, 'nome': '4.2 - Carnaúba (pó)'},
                            {'id': 3424, 'nome': '5.1 - Buriti'},
                            {'id': 3425, 'nome': '5.2 - Carnaúba'},
                            {'id': 3426, 'nome': '5.3 - Piaçava'},
                            {'id': 3429, 'nome': '6.1 - Balata'},
                            {'id': 3430, 'nome': '6.2 - Maçaranduba'},
                            {'id': 3431, 'nome': '6.3 - Sorva'},
                            {'id': 3433, 'nome': '7.1 - Carvão vegetal'},
                            {'id': 3434, 'nome': '7.2 - Lenha'},
                            {'id': 3435, 'nome': '7.3 - Madeira em tora'},
                            {'id': 3439, 'nome': '8.1 - Babaçu (amêndoa)'},
                            {'id': 3440, 'nome': '8.2 - Copaíba (óleo)'},
                            {'id': 3441, 'nome': '8.3 - Cumaru (amêndoa)'},
                            {'id': 3442, 'nome': '8.4 - Licuri (coquilho)'},
                            {'id': 3443, 'nome': '8.5 - Oiticica (semente)'},
                            {'id': 3444, 'nome': '8.6 - Pequi (amêndoa)'},
                            {'id': 3445, 'nome': '8.7 - Tucum (amêndoa)'},
                            {'id': 3448, 'nome': '9.1 - Pinheiro brasileiro (nó de pinho)'},
                            {'id': 3449, 'nome': '9.2 - Pinheiro brasileiro (árvores abatidas)'},
                            {'id': 3450, 'nome': '9.3 - Pinheiro brasileiro (madeira em tora)'},
                            {'id': 3452, 'nome': '10.1 - Angico (casca)'},
                            {'id': 3453, 'nome': '10.2 - Barbatimão (casca)'}
                        ]
                    }
                ],
                'ano_inicio': 1986,
                'ano_fim': datetime.now().year
            },
            {
                'id': 291,
                'nome': 'Quantidade produzida e valor da produção na silvicultura, por tipo de produto da silvicultura',
                'variaveis': [
                    {'id': 142, 'nome': 'Quantidade produzida na silvicultura'}, 
                    {'id': 143, 'nome': 'Valor da produção na silvicultura'}
                ],
                'classificacoes' : [
                    {
                        'id': 194,
                        'categorias': [
                            {'id': 33247, 'nome': '1.1.1 - Carvão vegetal de eucalipto'},
                            {'id': 33248, 'nome': '1.1.2 - Carvão vegetal de pinus'},
                            {'id': 33249, 'nome': '1.1.3 - Carvão vegetal de outras espécies'},
                            {'id': 33250, 'nome': '1.2.1 - Lenha de eucalipto'},
                            {'id': 33251, 'nome': '1.2.2 - Lenha de pinus'},
                            {'id': 33252, 'nome': '1.2.3 - Lenha de outras espécies'},
                            {'id': 33253, 'nome': '1.3.1.1 - Madeira em tora de eucalipto para papel e celulose'},
                            {'id': 33254, 'nome': '1.3.1.2 - Madeira em tora de pinus para papel e celulose'},
                            {'id': 33255, 'nome': '1.3.1.3 - Madeira em tora de outras espécies para papel e celulose'},
                            {'id': 33256, 'nome': '1.3.2.1 - Madeira em tora de eucalipto para outras finalidades'},
                            {'id': 33257, 'nome': '1.3.2.2 - Madeira em tora de pinus para outras finalidades'},
                            {'id': 33258, 'nome': '1.3.2.3 - Madeira em tora de outras espécies para outras finalidades'},
                            {'id': 3461, 'nome': '2.1 - Acácia-negra (casca)'},
                            {'id': 3462, 'nome': '2.2 - Eucalipto (folha)'},
                            {'id': 3463, 'nome': '2.3 - Resina'}
                        ]
                    }
                ],
                'ano_inicio': 1986,
                'ano_fim': datetime.now().year                
            }
        ]
    }
]
