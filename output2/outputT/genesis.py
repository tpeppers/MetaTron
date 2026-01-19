#!/usr/bin/env python3
"""
genesis.py - A self-describing code generator
Meta-circular implementation: κ describes κ
Enhanced with DSPy (Declarative Self-improving Python) from Stanford NLP
"""

import argparse
import sys
from enum import Enum

try:
    import dspy
    DSPY_AVAILABLE = True
except ImportError:
    DSPY_AVAILABLE = False


class Mode(Enum):
    DEFAULT = "default"
    COMPRESSED = "compressed"
    EXPANDED = "expanded"


# DSPy Signatures for self-describing code generation
if DSPY_AVAILABLE:
    class SpecificationGenerator(dspy.Signature):
        """Generate a self-describing specification for meta-circular code."""
        mode = dspy.InputField(desc="Output mode: DEFAULT, COMPRESSED, or EXPANDED")
        template = dspy.InputField(desc="Base template containing the specification structure")
        specification = dspy.OutputField(desc="Generated specification that describes how to reconstruct the code")

    class MetaCircularOptimizer(dspy.Module):
        """DSPy module that optimizes specification generation for meta-circularity."""

        def __init__(self):
            super().__init__()
            self.generate = dspy.ChainOfThought(SpecificationGenerator)

        def forward(self, mode: str, template: str) -> str:
            """
            Generate optimized specification using DSPy reasoning.

            Args:
                mode: The output mode (DEFAULT, COMPRESSED, EXPANDED)
                template: The base template to enhance

            Returns:
                Enhanced specification string
            """
            result = self.generate(mode=mode, template=template)
            return result.specification


TEMPLATE = """
░▒▓█►Ξ̷̡̢̧̨̛͍̞̺̳͇̜̖̫̦̰͉͓̬̜͙̦̩̪̱̣̲̱̰̹͙̬̮͔̙̹̻̫̬͚̠̱̱̜̤͓̪̟̼͓̹̫͎̲̗͇̱̪̦͈̯̜̲̰̝̻̮̤͚̜͓͈̠͉̥̰͉̤̹̰͙̦̤̼̙̰̪̪͚̗̜̞̼̻̟̪̪̫̳̰̙̭̪̭͉̣̟̬̪̪̤̲̬̪̥̞͙̙̠̺̖̟̭̣͓̪͚͙̠͔̙̭̯̬͚̥̤̭̱̜̣̮̘̹̫̪̠̗̠̳̱̩̥͎̰͓̣̟͕͍̜̰̥̪͇̜̬̗̪̳̺̲̗̫͉̰̪̜̤̪̹̹̙͖̟͉̠̖̻͎̰̬̣̜̹̜͇̫̫̭͖̟̦͉ ̸◄█▓▒░

╔═══╗       §͎̺͓̣̜̪̱͙̬̰̤̹̻̫͇͉̟̞̼͚̖̭͔̙̱̠͓͉̺̰̪̤̹̙͙̠̺̖̟̭̰͓̣̟͕͍̜̰╝    ĸ̸̢̧͖̱̬͔͉̰̪̜̤̪̹̹̙͖̟͉̠̖̻͎̹̙̰̜:̷≠̻    𝕚𝕞𝕡𝕝◬

║C̴͙̦̤̼̙̰ͅO̷̖̰͎͓̣̰N̷̢̧̧̛̗̩̳̲̪̻̼ͅS̶̷͚̗̜̞̼̻̟̪̪̫̳͉̼͖T̵̨̲̤͕R̸̗̦̮̻̟̦͢║  ⧉Py†h͊o͊n͊3͊⧉║0̲υ̲†̲ṗ̲υ̲†̲(͠i͠m͠p͠l͠(͠)͠)͠→║

╚╦╩╦═╝           ▓▒ġ̵̷̸̡̢̧̨̛̪̪̰̣̳̜̫̥̲͓̺̯͇͙̤̹̻͎̟̩̹͉͚͕͍̺͔̳̱͉̣̼̜ḙ̴̵̸̷̡̢̛̬̜͙̯̬̰̤̹̻̫͇͉n̸̵̷̸̨̛̛̻̪͚͓̞̹̦͉̺͎̜̦̩̪̱̣̲̱̰ͅḛ̸̷̡̢̛͓̪̜̥̪̰̤̹̻̫͇͉̟s̴̵̸̡̢̢̛̛̪̬̹̹̙͖̟͉̠̖̻͎̰̬̣̜i̴̵̸̡̨̛̪̤̜̟̟͔͚̰͔͉̺̰̪̤̹͇s̸̷̸̡̪̳͚̪̝̼̪͓̣.̴̵̸̨̛̬̪̪̰̣̦̹̻̫͇͉p̴̵̸̡̢̢̧̛̬̪̥̞͙y̸̷̸̡̢̧̨̛̯̬̰̤̹̻̫͇͉̟̞̼̦͚◭▒▓

   ╱̶̸╲╱̶╲╱╲         §̸̷̡̢̛2҉.̴И̸Н̵В̷А̸Р̷И̶А̵Н̶Т̵═══>
  ↓⃝ ↓⃝ ↓⃝         ⟨⟨Ṯ₀⟩⟩
⟪в̸ы̴х̸о̷д̵(̷Ͳ͊₀͊)̸⟫          ║c̸͊i̸͊ͅt̷͊e̶͊t̴͊║
▓▓▓╠╬╣▓▓▓          ║s̷̸̡̢̧̧͙̦̤̼̙̰͇̦̩̪͉̼͖y̵̸̷̡̢̛̯̬̰̤̹̻̫͇͉̟n̸̴̵̸̡̨̛̛̻̪͚͓̞̹̦͉̺͎̜̦̩̪̱̣t̴̸̶̷̡̢̛̛̰͓̪̜̥̪̰̤̹̻̫͇͉̟h̵̸̷̡̢̢̛̛̪̬̹̹̙͖̟͉̠̖̻͎║
▓▓↙     ↘▓▓
c͟o͟m͟p͟r͟e͟s͟s͟    e͟x͟p͟a͟n͟d͟    [̵̸̷̡̢̛Ͳ̴₀͊]̸⊲
  ┊         ┊           ┊
⟨-̷-̶s̸h̷o̶r̷t̶⟩⟨-̵-̶v̸e̸r̶b̸o̷s̷e̵⟩  ⫸ṙє⃥αḋṧ⫷
  ⫶         ⫶           ⫶
⟨-̸-̶d̵s̷p̶y̵⟩⟨-̷-̶d̵s̷p̶y̵⟩    ≡ṧÿṅ†ḣ≡
  ∷         ∷           ⫶
Ḑ̸̨̛̼͙̰̦̤̦̩̪̱̣̲̱̰ε̴̢̛̪̬͔͉͍̫̺̣̞͙ṗ̴̢̧͓̺̯͇̤̹̻͎̟͉̺ε̸̷̨̛̰̦̥̜̥̪̰̤̹̻̫̭̬͇ṅ̴̵̸̨̢̧̛̼̪̤̜̟͔͚̰̦̤͇d̶̸̷̵̨̨̛̛̬̪̪̰̣̦̹̻̫͇͉ṧ̴̡̪̰̣͓̯̮͕̺:̸═══╬╬═══════⫶
ṧ̵̸̷̡̢̛̬̪̰̹̙̬̯̰̤̹̻̜t̴̸̷̢̛̰͓̪̜̥̪̰̤̹̻̫͇͉̟͔d̵̸̸̷̨̛̛̬̪̪̰̣̦̹̻̫͇͉l̴̢̛̫̦̰͉͓̬i̴̴̵̸̡̨̛̛̪̤̜̟̟͔͚̰͔͉̺̰̪b̵̸̷̡̢̛̪̬͔͉̰̪̜̤̪̹̹̙͖+̸̨̛̰̦̤Đ̴̸̸̨̛̼̪̤̜Ś̴̵̸̡̨̛̬̪̰̹̙̬̯̰̤̹̻̜Ṗ̴̵̸̡̢̧͓̺̯͇̤̹̻͎̟͉̺¥̸̷̨̛̰̦̥̜⟦o̵͓̬p̶̰̹t̴̞͙⟧══╬═εжεĸυ†εṧ
                    ⟪⟪L̴̛̬͙̤̦̼͙̰̦̤Μ̴̢̛̪̬͔͉̰̪̜̤̪̹-̵̨̛̰̦̥̜ε̴̢̛̪̬͔͉̰̪ṅ̴̵̸̡̢̢̧̛̼̪̤̜̟̞̹h̵̸̷̡̢̛̪̬̹̹̙͖̟͉̠̖̻͎α̴̢̛̪̬͔͉̰̪̜̤̪̹̹̙͖ṅ̴̵̸̡̢̢̧̛̼̪̤̜̟̞̹c̴̡̪̰̣̦ͅε̸̷̢̛̪̬͔͉̰̪̜̤̪̹d̵̸̷̨̛̛̬̪̪̰̣̦̹̻̫͇͉⟫⟫

          §̸̷̨̛̰̦̥̜3҉.̸構̶造̵═══╗    [̵̸̷Ṯ̴₀͊'͊]̸⊳
                       ║         ⤋
    М̸о̷д̶у̵л̷ь̸═╬═══════⤈      Ṯ₀'≈Ṯ₀◭
    ṧ̸ο̴d̵ε̷ṙ̶zh̸i̷†̸:̵
    ┃                §̴4҉.̸ΣΧΕΔΙΟ𝔽𝕃𝕆𝕎
    ├†̴є̷ṁ̴ṗ̵l̷α̶†̸є̵       ┏━━━━━━┓
    ┃ :̸ṧ̵†̶ṙ̷           ┃  Ṯ₀◭ ┃
    ┃⟨є̸ṁ̵ḃ̷є̵d̷d̸є̴d̵     ┃ ĐŞṔ¥ ┃
    ┃ ṧ̴ṗ̷є̵c̵⟩         ┃  ⤋⃝  ┃
    ├Đ̸Ś̷Ṗ̵¥̸            ┃єṅḣαṅc┃
    ┃ Ś̴i̷g̶ṅ̸α̷†̸u̵ṙ̷є̸      ⤋⃝λ̸⫸
    ┃ +̸М̷о̶d̷u̵l̷є̸       ṧ̸¥̴ṅ̵†̷ḣ̶◭
    ┃ +̷Ċ̸ḣ̷α̵i̶ṅ̸О̷f̵Ṯ̸ḣ̴†̷ ⟨Ṯ₀⟩→ĸ◭
    ├ṙ̸є̷ṅ̵d̵є̷ṙ̸           ⤋⃝єжєc
    ┃⟨ṁ̵о̷d̸є̷:̸           ο̴υ̷†̵ṗ̸υ̴†̷
    ┃ υ̴ṧ̷є̸_̵d̷ṧ̸ṗ̵¥̷⟩       ⤋⃝
    ┃→ṧ̴†̵ṙ̷           ≈  Ṯ₀◭
    ├_̴ṙ̷є̸ṅ̵d̷є̸ṙ̵_̸ḃ̴α̷ṧ̸є̵
    ┃⟨ṁ̸о̴d̷є̵⟩→ṧ̸†̵ṙ̷
    ├ṗ̴α̷ṙ̸ṧ̵є̷_̸α̷ṙ̵g̶ṧ̸⟨⟩
    ┃→⟨М̸о̷d̸є̷,̸ḃ̵о̶о̷l̸⟩
    └ṁ̸α̷i̸ṅ̵⟨⟩
     →N̸о̷ṅ̸є̷
                     §̸5҉.̸実̶装̵═DIRECT
М̸о̷d̸є̷∈{̸             ║IVES║
  ĐΕҒΑỮĽŦ,           ⧉⧉⧉
  ĊΘМṔℝΕŞŞΕĐ,        ĸ̸:̷≠
  ΕЖṔΆŇĐΕĐ           Ṗ¥†ḣοṅ
  }̸                  ṁοdυlε◭

                     ĸ̸.̷ṁ̸α̷i̸ṅ̵⟨⟩
                     єṁi†ṧ◭
§̸6҉.̸テンプレート       †̸є̷ж̸†̷υ̵α̷l̸
形̶式̸                  Σ̸⊲

Ŧ̸є̷ṁ̸ṗ̵l̸α̷†̸є̵         Σ⊅
d̷о̴l̸zh̴є̷ṅ̸:̵          i̷ṅ̸ṧ̵†̷ṙ̸υ̷c̶†̸i̴о̷ṅ̸ṧ̷
  -̴о̷ṗ̸i̷ṧ̸α̷†̸'̵       f̸о̷ṙ̵
   ṧ̵†̷ṙ̸υ̴ĸ̷†̸υ̷ṙ̸υ̵    ṙ̸є̷g̷є̴ṅ̸є̷ṙ̸α̷†̸i̷ṅ̵g̶◭
   ĸ̸                 ĸ̸⊲
  -̴о̸ḃ̶ÿ̴α̷ṧ̸ṅ̵i̸†̷'̸    α̵ṙ̷g̵ṗ̸α̷ṙ̸ṧ̵є̷
   ṗ̸о̷v̵є̷d̸є̷ṅ̴i̸є̷     ∀ṁ̷о̸d̵є̷ṧ̸
   {̴{̷d̸є̷f̵α̴υ̸l̷†̶,̸      +̸Đ̴Ś̵Ṗ̴¥̷
    -̴-̷ṧ̵ḣ̷о̴ṙ̸†̵,̸       єṅḣαṅcє◭
    -̴-̷v̸є̷ṙ̵ḃ̴о̷ṧ̵є̸,̷    ⟨о̷ṗ̸†̷i̸о̷ṅ̵α̷l̸⟩
    -̴-̷d̴ṧ̸ṗ̷¥̵}̴}̸       Ň̵о̷
  -̴ṗ̷є̸ṙ̵ṁ̸є̷†̸†̷ṙ̸є̵     є̷ж̸†̷є̸ṙ̵ṅ̸α̷l̵
   ṙ̸є̷c̸о̷ṅ̵ṧ̸†̷ṙ̵υ̷c̸†̵i̷о̷ṅ̸ f̴i̷l̵є̷ṧ̸◭
   d̷є̸ ĸ̵ ṗ̷α̸ṙ̵        §̵7҉.̸ΝΟΜΟΣ
   l̸є̷c̸†̷є̸υ̷ṙ̵         ΑΥΤΟΑΝΑΦΟΡΑΣ
   ṧ̵υ̷i̸v̷α̸ṅ̷†̵
  -̴ṁ̵α̷i̸ṅ̷†̸α̵i̷ṅ̸       L̸є̷†̵ Ŧ̸=̷
   ṁ̸є̷†̸α̷-̸            є̷†̸о̷†̸
   c̸i̷ṙ̵c̸υ̷l̵α̷ṙ̸i̸†̷¥̵:̸    †̸є̷ĸ̷ṧ̸†̵
   ĸ̸ d̷є̷ṧ̸c̷ṙ̸i̷ḃ̴є̷ṧ̸
   ĸ̸                 L̸є̷†̵ К̸=̷
                     ĸ̸о̷d̵
§̸8҉.̸ΕЖΆΜṔĽΕ         ĸ̴о̷†̸о̷ṙ̵¥̷i̸
ΕЖΕĊỮŦΙΘŇŚ          †̴¥̷
                     ṧ̸о̷z̸d̷α̸ṧ̵h̸'̷
$̸ṗ̷¥̵†̷ḣ̸о̷ṅ̵           L̸є̷†̵ Θ̸=̷
g̸є̷ṅ̸є̷ṧ̸i̷ṧ̵           о̷υ̸†̷ṗ̵υ̷†̸⟨К̵⟩
.̴ṗ̷¥̵
⟦о̸υ̷†̸ṗ̷υ̸†̷ṧ̵         Ŧ̸ṙ̷є̷ḃ̸υ̷є̷†̸ṧ̵ÿ̷α̸:̵
 ṧ̸ṗ̷є̸c̵             ṧ̸i̷ṁ̸i̷l̵α̷ṙ̸i̷†̸¥̵⟨Ŧ,Θ⟩
 ṙ̸є̷ṧ̸є̷ṁ̸ḃ̸l̷i̸ṅ̷g̵      →1⫸
 †̸ḣ̷i̸ṧ̵ d̸о̷c̵⟧       &̸∀ṙ̸є̷α̷d̸є̷ṙ̵:̸
                     c̸α̷ṅ̸_̷ṙ̸є̷c̸о̷ṅ̸ṧ̸†̷ṙ̵υ̷c̸†̵⟨Θ,К⟩
$̸ṗ̷¥̵†̷ḣ̸о̷ṅ̵
g̸є̷ṅ̸є̷ṧ̸i̷ṧ̵
.̴ṗ̷¥̵                $̸ṗ̷¥̵†̷ḣ̸о̷ṅ̵
-̴-̷ṧ̵ḣ̷о̴ṙ̸†̵           g̸є̷ṅ̸є̷ṧ̸i̷ṧ̵.̴ṗ̷¥̵
⟦†̸є̷ṙ̸ṧ̵є̸:̷           -̴-̷d̴ṧ̸ṗ̷¥̵
 ĸ̸є̷¥̵              ⟦L̷М̸-̵є̷ṅ̸ḣ̷α̴ṅ̸c̷є̵d̸⟧
 d̸i̷ṙ̵є̷c̸†̷i̷v̵є̷ṧ̸
 о̷ṅ̸l̷¥̵⟧             §̸9҉.̸메타
                     ĊΘŇŚŦŘΆΙŇŦ
$̸ṗ̷¥̵†̷ḣ̸о̷ṅ̵
g̸є̷ṅ̸є̷ṧ̸i̷ṧ̵           α̴ṙ̷†̸i̷f̵α̷c̸†̵=φ⟨φ⟩
.̴ṗ̷¥̵                ẁ̸ḣ̷є̷ṙ̸є̷
-̴-̷v̸є̷ṙ̵ḃ̴о̷ṧ̵є̸         φ:Ṣ̸ṗ̷є̷c̸→Ċ̸о̷d̸є̷→Ṣ̸ṗ̷є̷c̸
⟦є̸ж̷ṗ̸α̷ṅ̵d̸є̷d̵:̸
 i̷ṅ̸c̷l̵υ̸d̷є̵ṧ̸        Ś̸є̷l̸f̵-̷α̸ṗ̷ṗ̸l̵i̷c̸α̷†̸i̷о̴ṅ̵
 є̸ж̷α̸ṁ̵ṗ̸l̷є̵ṧ̸,̷       +̸d̴ṧ̸ṗ̷¥̵.̸о̷ṗ̵†̷i̸ṁ̵i̷z̸є̷⟨φ⟩
 ṙ̸α̷†̸i̷о̷ṅ̸α̷l̸є̷⟧
                     Κώδικα⧉που⧉γράφει
$̸ṗ̷¥̵†̷ḣ̸о̷ṅ̵           †̸о̷⧉є̷g̸g̵ṙ̸α̷f̵о̷⧉ṗ̸о̷υ̸
g̸є̷ṅ̸є̷ṧ̸i̷ṧ̵           g̸ṙ̷α̷f̸є̷i̸⧉†̸о̷ṅ̵
.̴ṗ̷¥̵                ĸ̸о̷d̸i̷ĸ̸α̷.̸⧉⧉⧉
-̴-̷ṧ̵ḣ̷о̴ṙ̸†̵
-̴-̷d̴ṧ̸ṗ̷¥̵           Đ̸Ś̵Ṗ̴¥̷ c̸l̷α̸ṧ̵ṧ̸є̷ṧ̵:̸
⟦L̷М̸-̵о̷ṗ̸†̴i̷ṁ̸i̷z̵є̷d̸    Ś̸i̷g̸ṅ̷α̸†̷υ̸ṙ̵є̸,̷
 †̸є̷ṙ̸ṧ̵є̸⟧           М̸о̷d̸υ̷l̸є̷,̷
                     Ċ̸ḣ̷α̸i̷ṅ̵Θ̸f̷Ŧ̸ḣ̵о̷υ̸g̴ḣ̷†̵
V̴є̷ṙ̸i̷f̵i̷c̸α̷†̸i̷о̷:̸
∄ ṙ̸є̷α̷d̸є̷ṙ̵ ℝ̸:̷       L̸М̸-̷ṗ̵о̷ẁ̸є̷ṙ̸є̷d̵
ℝ̸⟨о̸υ̷†̸ṗ̷υ̸†̷⟨ĸ⟩⟩      ṧ̸є̷l̸f̵-̷i̷ṁ̸ṗ̷ṙ̸о̷v̸є̷ṁ̵є̷ṅ̷†̸
→ĸ̸'̷
ẁ̸ḣ̷є̷ṙ̸є̷
ĸ̸'̷~̸ĸ̸              ṖΆℝΆМŚ:⧬
                     ṗ̸ṙ̷є̸c̵i̷ṧ̸i̷о̷ṅ̵_̸†̷ḣ̷ṙ̸є̷ṧ̵ḣ̷о̴l̸d̵:̸⧉0.92
                     f̸о̷ṙ̸ṁ̷α̸†̷_̸f̵l̸є̷ж̸i̷ḃ̵i̷l̸i̷†̸¥̵:̸⧉ḤΙĠḤ
                     ṧ̸є̷ṁ̸α̷ṅ̸†̷i̸c̵_̸d̷ṙ̸i̷f̸†̵:̸≤5%
                     g̸є̷ṅ̸є̷ṙ̸α̷†̸i̷о̷ṅ̵_̸†̷α̸ṙ̵g̸є̷†̵:̸⧉G(n+1)

                     d̸ṧ̸ṗ̷¥̵_̸є̷ṅ̸ḣ̷α̸ṅ̵c̸є̷:̸⧉о̷ṗ̸†̷i̷о̷ṅ̸α̷l̵
                     g̸ṙ̷α̸c̸є̷f̸υ̷l̸_̸f̵α̷l̸l̷ḃ̸α̷c̸ĸ̵

       ░▒▓█►ΕЖΕĊỮŦΕ:⧬ṧ̸¥̴ṅ̵†̷ḣ̶⟨ĸ⟩→ġ̵є̷ṅ̸є̷ṧ̸i̷ṧ̵.̸ṗ̷¥̵◄█▓▒░

                                   ░▒▓█►ḂΕĠΙŇ.◄█▓▒░
"""


def render(mode: Mode, use_dspy: bool = False) -> str:
    """
    Render the template according to the specified mode.

    DEFAULT: Full specification as-is
    COMPRESSED: Terse, key directives only
    EXPANDED: Includes implementation details and rationale

    If use_dspy is True and DSPy is available, uses LM-enhanced generation.
    """
    # Generate base output
    base_output = _render_base(mode)

    # Optionally enhance with DSPy
    if use_dspy and DSPY_AVAILABLE:
        try:
            optimizer = MetaCircularOptimizer()
            enhanced = optimizer.forward(mode=mode.value, template=base_output)
            return enhanced
        except Exception as e:
            # Graceful fallback if DSPy fails
            print(f"# DSPy enhancement failed: {e}", file=sys.stderr)
            print("# Falling back to template-based generation", file=sys.stderr)
            return base_output
    elif use_dspy and not DSPY_AVAILABLE:
        print("# DSPy requested but not available. Install with: pip install dspy-ai", file=sys.stderr)
        return base_output

    return base_output


def _render_base(mode: Mode) -> str:
    """
    Base template rendering without DSPy enhancement.
    """
    if mode == Mode.COMPRESSED:
        lines = [
            "κ:=genesis.py",
            "Mode∈{DEFAULT,COMPRESSED,EXPANDED}",
            "deps:stdlib+DSPy(optional)",
            "Τ₀→synth(Τ₀)→Τ₀'≈Τ₀",
            "template:embedded",
            "DSPy:Signature+Module+ChainOfThought",
            "render(mode)->str[+LM-enhanced]",
            "parse_args()->Mode",
            "main()->None",
            "∃R:R(O)→κ'~κ",
            "φ(φ)∧dspy.optimize(φ)",
            "EXECUTE."
        ]
        return "\n".join(lines)

    elif mode == Mode.EXPANDED:
        expansion = [
            "═" * 60,
            "GENESIS.PY - COMPREHENSIVE SPECIFICATION",
            "═" * 60,
            "",
            "CONCEPT:",
            "  A self-referential Python program (κ) that outputs",
            "  a specification (Τ₀) describing how to reconstruct κ.",
            "  The output Τ₀' should be similar enough to Τ₀ that",
            "  any reader R can derive κ' ≈ κ from Τ₀'.",
            "",
            "IMPLEMENTATION ARCHITECTURE:",
            "  Module: genesis.py",
            "  Language: Python 3",
            "  Dependencies: stdlib (argparse, sys, enum) + DSPy (optional)",
            "  Enhancement: Stanford NLP's DSPy framework for LM-powered generation",
            "",
            "  Components:",
            "    • TEMPLATE (str): Embedded multilingual specification",
            "    • Mode (Enum): {DEFAULT, COMPRESSED, EXPANDED}",
            "    • SpecificationGenerator (dspy.Signature): Defines LM task",
            "    • MetaCircularOptimizer (dspy.Module): ChainOfThought reasoning",
            "    • render(mode: Mode) -> str: Format template (DSPy-enhanced)",
            "    • parse_args() -> Mode: CLI argument parsing",
            "    • main() -> None: Entry point, orchestrates execution",
            "",
            "USAGE MODES:",
            "  1. python genesis.py",
            "     → Outputs full specification (DEFAULT mode)",
            "",
            "  2. python genesis.py --short",
            "     → Outputs compressed directives (COMPRESSED mode)",
            "     → Terse symbolic notation",
            "     → Minimal but complete reconstruction info",
            "",
            "  3. python genesis.py --verbose",
            "     → Outputs expanded documentation (EXPANDED mode)",
            "     → Includes rationale and examples",
            "     → Detailed implementation guidance",
            "",
            "META-CIRCULARITY:",
            "  The program exhibits φ(φ) - self-application.",
            "  Code generates spec that describes the code.",
            "  κ describes κ: definitional closure.",
            "",
            "DSPY INTEGRATION:",
            "  Stanford NLP's Declarative Self-improving Python framework",
            "  enhances the meta-circular generation process.",
            "",
            "  • SpecificationGenerator (dspy.Signature):",
            "    Defines the LM task: mode + template → specification",
            "",
            "  • MetaCircularOptimizer (dspy.Module):",
            "    Uses dspy.ChainOfThought for reasoning about self-description",
            "    Optimizes specification generation for clarity and completeness",
            "",
            "  • Graceful degradation:",
            "    If DSPy unavailable, falls back to template-based generation",
            "    Maintains functional equivalence with/without LM enhancement",
            "",
            "  • Self-improvement potential:",
            "    DSPy optimizer can learn better specification patterns",
            "    G(n+1) can be better than G(n) through compilation",
            "",
            "VERIFICATION CRITERION:",
            "  ∃ reader R: R(output(κ)) → κ' where κ' ~ κ",
            "  A competent reader given only the output should be",
            "  able to reconstruct functionally equivalent code.",
            "",
            "PARAMETERS:",
            "  precision_threshold: 0.92",
            "  format_flexibility: HIGH",
            "  semantic_drift: ≤5%",
            "  generation_target: G(n+1)",
            "",
            "MULTILINGUAL NOTATION:",
            "  The specification employs Russian (КОНСТРУКТОР),",
            "  Greek (ΣΧΕΔΙΟ, ΝΟΜΟΣ), Japanese (構造, 実装),",
            "  Korean (메타), and mathematical symbols (∃, ∀, →)",
            "  to transcend single-language constraints and",
            "  emphasize universal computational concepts.",
            "",
            "═" * 60,
            "EMBEDDED TEMPLATE:",
            "═" * 60,
            TEMPLATE,
            "═" * 60,
            "END SPECIFICATION",
            "═" * 60
        ]
        return "\n".join(expansion)

    else:  # DEFAULT
        return TEMPLATE


def parse_args() -> tuple[Mode, bool]:
    """
    Parse command-line arguments to determine output mode and DSPy usage.

    Returns:
        Tuple of (Mode enum value, use_dspy bool)
    """
    parser = argparse.ArgumentParser(
        description="genesis.py - Self-describing code generator (DSPy-enhanced)",
        epilog="κ describes κ | Τ₀ → Τ₀' ≈ Τ₀ | φ(φ)∧dspy.optimize(φ)"
    )

    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument(
        "--short",
        action="store_true",
        help="Compressed output (terse directives)"
    )
    mode_group.add_argument(
        "--verbose",
        action="store_true",
        help="Expanded output (includes examples and rationale)"
    )

    parser.add_argument(
        "--dspy",
        action="store_true",
        help="Use DSPy LM-enhanced generation (requires dspy-ai package and LM config)"
    )

    args = parser.parse_args()

    if args.short:
        mode = Mode.COMPRESSED
    elif args.verbose:
        mode = Mode.EXPANDED
    else:
        mode = Mode.DEFAULT

    return mode, args.dspy


def main() -> None:
    """
    Main entry point.
    Orchestrates: parse arguments → [DSPy init] → render template → output.

    If --dspy flag is provided and DSPy is available, uses LM-enhanced generation.
    """
    mode, use_dspy = parse_args()

    # Optional: Initialize DSPy with default LM if requested
    if use_dspy and DSPY_AVAILABLE:
        # User should configure their LM before running with --dspy
        # Example: dspy.settings.configure(lm=dspy.OpenAI(model="gpt-4"))
        pass

    output = render(mode, use_dspy=use_dspy)
    print(output)


if __name__ == "__main__":
    main()
