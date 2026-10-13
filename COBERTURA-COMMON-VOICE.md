# Cobertura de Common Voice — versión 0.3.0

Comprebación: 13-10-2026, Hunspell 1.7.2, corpus de 10.460 ringleras.

| Mida | Resultau |
|---|---:|
| Ocurrencias de parolas evaluadas | 86.783 |
| Ocurrencias reconoixidas | 76.941 |
| Ocurrencias sin reconoixer | 9.842 |
| **Cobertura por ocurrencias** | **88,66 %** |
| Proporción sin reconoixer | 11,34 % |
| Formas distintas evaluadas, distinguindo mayusclas | 13.205 |
| Formas distintas reconoixidas | 7.068 |
| Cobertura por formas distintas | 53,53 % |

La cifra principal pondera per frecuencia: cada aparición d'una parola conta. La cifra de formas distintas da lo mesmo peso a una forma que amaneixe una vegada y a unatra muito frecuent; son medidas diferents.

Formula: 100 × reconoixidas / (reconoixidas + desconoixidas).

S'executan Hunspell `-G` y `-l` sobre lo mesmo texto con o mesmo diccionario, codificación UTF-8 y sin diccionario personal predeterminau. Se conserva la suya segmentación nativa; los signos y numeros que no reporta no dentran en o denominador. Los apóstrofos pueden dividir las parolas en components. Las dos listas de formas reconoixidas y desconoixidas no se solapan en esta mida.

La cobertura no ye un percentache de corrección normativa ni gramatical: puede haber-ie formas correctas ausents, erratas presents en o corpus y parolas reconoixidas pero inadecuadas en contexto. Esta revisión no mide totas las posibles falsas acceptacions.

En a primera preba i heba 17.048 ocurrencias sin reconoixer; agora i hai 9.842, una reducción neta de 7.206 (42,3 %). Este percentache de reducción ye diferent d'a cobertura final d'o 88,66 %.

Resultaus y SHA-256 d'o texto/diccionario en `../corpus-results/frases_pa_hunspell/0.3/summary.json`; listas completas en `recognized-occurrences.txt` y `unknown-occurrences.txt` d'ixe directorio. Lo calculo se reproduz per medio de `check_corpus.py`.

La cobertura inicial yera d'o 80,36 % (69.735 ocurrencias reconoixidas); la final aconsigue lo 88,66 %, una millora de 8,30 %.