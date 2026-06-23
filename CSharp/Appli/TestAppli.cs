using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Math = System.Math;
namespace Test_App
{
    internal class Program
    {
        abstract class Operation
        {
            public abstract float Calcul(float a, float b);
            public abstract string GetName();
        }
        class Addition : Operation
        {
            public override float Calcul(float a, float b)
            {
                return a + b;
            }

            public override string GetName()
            {
                return "Addition";
            }
        }
        class Soustraction : Operation
        {
            public override float Calcul(float a, float b)
            {
                return a - b;
            }

            public override string GetName()
            {
                return "Soustraction";
            }
        }
        class Multiplication : Operation
        {
            public override float Calcul(float a, float b)
            {
                return a * b;
            }

            public override string GetName()
            {
                return "Multiplication";
            }
        }
        class Division : Operation
        {
            public override float Calcul(float a, float b)
            {
                return a / b;
            }

            public override string GetName()
            {
                return "Division";
            }
        }
        class Reste : Operation
        {
            public override float Calcul(float a, float b)
            {
                return a % b;
            }

            public override string GetName()
            {
                return "Reste";
            }
        }
        abstract class Fonctions
        {
            public abstract float Fonction(float a);
            public abstract string GetName();
        }
        class Carre : Fonctions
        {
            public override float Fonction(float a)
            {
                return (float)Math.Pow(a, 2);
            }

            public override string GetName()
            {
                return "Carre";
            }
        }
        class Cube : Fonctions
        {
            public override float Fonction(float a)
            {
                return (float)Math.Pow(a, 3);
            }

            public override string GetName()
            {
                return "Cube";
            }
        }
        class Inverse : Fonctions
        {
            public override float Fonction(float a)
            {
                return 1 / a;
            }

            public override string GetName()
            {
                return "Inverse";
            }
        }
        class Racine : Fonctions
        {
            public override float Fonction(float a)
            {
                if (a < 0)
                    return float.NaN;
                return (float)Math.Sqrt(a);
            }
            public override string GetName()
            {
                return "Racine Carrée";
            }
        }
        class Absolue : Fonctions
        {
            public override float Fonction(float a)
            {
                return (float)Math.Abs(a);
            }

            public override string GetName()
            {
                return "Valeur Absolue";
            }
        }
        

        static void Main(string[] args)
        {
            string asciiApp = @"
  /$$$$$$                      /$$ /$$                       /$$     /$$                    
 /$$__  $$                    | $$|__/                      | $$    |__/                    
| $$  \ $$  /$$$$$$   /$$$$$$ | $$ /$$  /$$$$$$$  /$$$$$$  /$$$$$$   /$$  /$$$$$$  /$$$$$$$ 
| $$$$$$$$ /$$__  $$ /$$__  $$| $$| $$ /$$_____/ |____  $$|_  $$_/  | $$ /$$__  $$| $$__  $$
| $$__  $$| $$  \ $$| $$  \ $$| $$| $$| $$        /$$$$$$$  | $$    | $$| $$  \ $$| $$  \ $$
| $$  | $$| $$  | $$| $$  | $$| $$| $$| $$       /$$__  $$  | $$ /$$| $$| $$  | $$| $$  | $$
| $$  | $$| $$$$$$$/| $$$$$$$/| $$| $$|  $$$$$$$|  $$$$$$$  |  $$$$/| $$|  $$$$$$/| $$  | $$
|__/  |__/| $$____/ | $$____/ |__/|__/ \_______/ \_______/   \___/  |__/ \______/ |__/  |__/
          | $$      | $$                                                                    
          | $$      | $$                                                                    
          |__/      |__/                                                                    ";
            string asciiCalc = @"
  /$$$$$$            /$$                     /$$             /$$               /$$                              
 /$$__  $$          | $$                    | $$            | $$              |__/                              
| $$  \__/  /$$$$$$ | $$  /$$$$$$$ /$$   /$$| $$  /$$$$$$  /$$$$$$    /$$$$$$  /$$  /$$$$$$$  /$$$$$$$  /$$$$$$ 
| $$       |____  $$| $$ /$$_____/| $$  | $$| $$ |____  $$|_  $$_/   /$$__  $$| $$ /$$_____/ /$$_____/ /$$__  $$
| $$        /$$$$$$$| $$| $$      | $$  | $$| $$  /$$$$$$$  | $$    | $$  \__/| $$| $$      | $$      | $$$$$$$$
| $$    $$ /$$__  $$| $$| $$      | $$  | $$| $$ /$$__  $$  | $$ /$$| $$      | $$| $$      | $$      | $$_____/
|  $$$$$$/|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$|  $$$$$$$  |  $$$$/| $$      | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$
 \______/  \_______/|__/ \_______/ \______/ |__/ \_______/   \___/  |__/      |__/ \_______/ \_______/ \_______/
                                                                                                                
                                                                                                                
                                                                                                                ";
            string asciiJeu = @"
    /$$$$$                       /$$                       /$$$$$$$           /$$          
   |__  $$                      | $$                      | $$__  $$         |__/          
      | $$ /$$   /$$  /$$$$$$$ /$$$$$$    /$$$$$$         | $$  \ $$ /$$$$$$  /$$ /$$   /$$
      | $$| $$  | $$ /$$_____/|_  $$_/   /$$__  $$ /$$$$$$| $$$$$$$//$$__  $$| $$|  $$ /$$/
 /$$  | $$| $$  | $$|  $$$$$$   | $$    | $$$$$$$$|______/| $$____/| $$  \__/| $$ \  $$$$/ 
| $$  | $$| $$  | $$ \____  $$  | $$ /$$| $$_____/        | $$     | $$      | $$  >$$  $$ 
|  $$$$$$/|  $$$$$$/ /$$$$$$$/  |  $$$$/|  $$$$$$$        | $$     | $$      | $$ /$$/\  $$
 \______/  \______/ |_______/    \___/   \_______/        |__/     |__/      |__/|__/  \__/
                                                                                           
";
            string asciiMeteo = @"
 /$$      /$$             /$$                        
| $$$    /$$$            | $$                        
| $$$$  /$$$$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
| $$ $$/$$ $$ /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$
| $$  $$$| $$| $$$$$$$$  | $$    | $$$$$$$$| $$  \ $$
| $$\  $ | $$| $$_____/  | $$ /$$| $$_____/| $$  | $$
| $$ \/  | $$|  $$$$$$$  |  $$$$/|  $$$$$$$|  $$$$$$/
|__/     |__/ \_______/   \___/   \_______/ \______/ 
                                                     
";
            string asciiExit = @"
 /$$$$$$$$           /$$   /$$    
| $$_____/          |__/  | $$    
| $$       /$$   /$$ /$$ /$$$$$$  
| $$$$$   |  $$ /$$/| $$|_  $$_/  
| $$__/    \  $$$$/ | $$  | $$    
| $$        >$$  $$ | $$  | $$ /$$
| $$$$$$$$ /$$/\  $$| $$  |  $$$$/
|________/|__/  \__/|__/   \___/  
                                  
";
            PrintBanner(asciiApp, ConsoleColor.Red);
            while (true)
            {
                //Interface de base
                if (!Saisir("===  Test_App  === \n1: Calculatrice \n2: Juste Prix \n3: Convertisseur °C/°F\n4: Quitter \nChoix: " , out int ActionChoice, 4))
                {
                    //"Choix" sera un bouton input et le reste des propositions seront soit un log si TUI ou juste component si UI 
                    continue;
                }
                    
                switch (ActionChoice)
                {
                    case 1:
                        //Calculatrice
                        PrintBanner(asciiCalc, ConsoleColor.Cyan);
                        bool quitCalc = false;
                        List<Operation> operations = new List<Operation>();
                        operations.Add(new Addition());
                        operations.Add(new Soustraction());
                        operations.Add(new Multiplication());
                        operations.Add(new Division());
                        operations.Add(new Reste());


                        List<Fonctions> fonctions = new List<Fonctions>();
                        fonctions.Add(new Carre());
                        fonctions.Add(new Cube());
                        fonctions.Add(new Inverse());
                        fonctions.Add(new Racine());
                        fonctions.Add(new Absolue());


                        while (!quitCalc)
                        {
                            global::System.Console.WriteLine("#######################");
                            global::System.Console.WriteLine();
                            string message = "-----[1]: Opérateur---- " +
                                "\n-----[2]: Puissances--- " +
                                "\n-----[3]: Fonctions---- " +
                                "\n-----[4]: Quit--------- " +
                                "\nChoix: ";
                            if (!Saisir(message, out int choix, 4))
                                continue;
                            switch (choix)
                            {
                                case 1:
                                    message = "-------Opérateur-------";
                                    for (int i = 0; i < operations.Count; i++)
                                    {
                                        Operation op = operations[i];
                                        message += "\n[" + (i + 1) + "] " + op.GetName();
                                    }
                                    message += "\nChoix: ";
                                    if (!Saisir(message, out int choix_operateur, operations.Count))
                                        continue;
                                    Console.WriteLine("-----------------------");
                                    Console.Write("a: ");
                                    float a_ope = Convert.ToSingle(Console.ReadLine());
                                    Console.Write("b: ");
                                    float b = Convert.ToSingle(Console.ReadLine());
                                    Console.WriteLine();
                                    Console.WriteLine("Result: " + operations[choix_operateur - 1].Calcul(a_ope, b));
                                    break;
                                case 2:
                                    Console.WriteLine("-------Puissances------");
                                    if (!Saisir("a: ", out int a))
                                        continue;
                                    if (!Saisir("n: ", out int n))
                                        continue;
                                    Console.WriteLine();
                                    Console.WriteLine("Result de " + a + "^" + n + " : " + (float)Math.Pow(a, n));
                                    break;
                                case 3:
                                    message = "-------Fonctions-------";
                                    for (int i = 0; i < fonctions.Count; i++)
                                    {
                                        Fonctions op = fonctions[i];
                                        message += "\n[" + (i + 1) + "] " + op.GetName();
                                    }
                                    message += "\nChoix: ";
                                    if (!Saisir(message, out int choix_fonctions, fonctions.Count))
                                        continue;
                                    Console.WriteLine("-----------------------");
                                    if (!Saisir("x: ", out float x))
                                        continue;
                                    Console.WriteLine();
                                    Console.WriteLine("Result: " + fonctions[choix_fonctions - 1].Fonction(x));
                                    break;
                                case 4:
                                    Console.WriteLine("Au revoir !");
                                    quitCalc = true;
                                    break;
                            }
                        }
                        break;
                    case 2:
                        //Juste Prix
                        PrintBanner(asciiJeu, ConsoleColor.Magenta);
                        Random random = new Random();
                        int nbGuess = 5;
                        int randomMax = 51;
                        bool hasWon = false;

                        int valueToGuess = random.Next(0, randomMax);
                        while (nbGuess > 0 && !hasWon)
                        {
                            if (Saisir("Ton guess: ", out int guess, randomMax))
                            {
                                int ecart = Math.Abs(valueToGuess - guess);
                                if (ecart <= 1)
                                {
                                    hasWon = true;
                                    Console.ForegroundColor = ConsoleColor.Green;
                                    Console.WriteLine("Tu as gagné !");
                                    Console.ResetColor();
                                }
                                else
                                {
                                    // Indication de chaleur selon l'écart
                                    string chaleur = ecart < 2 ? "BRÛLANT !" : ecart < 5 ? "Chaud" : ecart < 10 ? "Tiède" : "Froid";
                                    ConsoleColor couleur = ecart < 2 ? ConsoleColor.Red : ecart < 5 ? ConsoleColor.Yellow : ecart < 10 ? ConsoleColor.DarkYellow : ConsoleColor.Blue;
                                    string direction = valueToGuess > guess ? "supérieure" : "inférieure";
                                    Console.ForegroundColor = couleur;
                                    Console.WriteLine($"{chaleur} - La valeur est {direction}");
                                    Console.ResetColor();
                                }
                            }
                            else
                            {
                                continue;
                            }

                            nbGuess--;
                            Console.WriteLine(nbGuess + " / 5 essai(s) restant(s). ");
                        }

                        if (hasWon)
                        {
                            Console.ForegroundColor = ConsoleColor.Green;
                            Console.WriteLine("Fin du jeu, merci d'y avoir joué ! Vous avez gagné ! La valeur était : " + valueToGuess);
                            Console.ResetColor();
                        }
                        else
                        {
                            Console.ForegroundColor = ConsoleColor.Red;
                            Console.WriteLine("Fin du jeu, merci d'y avoir joué ! Vous avez perdu. La valeur était : " + valueToGuess);
                            Console.ResetColor();
                        }
                        break;
                    case 3:
                        // Convertisseur °C <-> °F
                        PrintBanner(asciiMeteo, ConsoleColor.Green);
                        Console.WriteLine("------Convertisseur------");
                        Console.WriteLine("1: °C -> °F");
                        Console.WriteLine("2: °F -> °C");
                        if (!Saisir("Choix: ", out int convChoice, 2))
                        {
                            break;
                        }
                        Console.Write("Température: ");
                        string tempS = Console.ReadLine();
                        if (!float.TryParse(tempS, out float tempVal))
                        {
                            Console.WriteLine("Valeur invalide.");
                            break;
                        }

                        if (convChoice == 1)
                        {
                            float resultF = tempVal * 9f / 5f + 32f;
                            Console.WriteLine($"{tempVal} °C = {resultF} °F");
                        }
                        else
                        {
                            float resultC = (tempVal - 32f) * 5f / 9f;
                            Console.WriteLine($"{tempVal} °F = {resultC} °C");
                        }
                        break;
                    case 4:
                        //Quit
                        PrintBanner(asciiExit, ConsoleColor.DarkGray);
                        return;
                }
            }
        }
        static bool Saisir(string message, out int userChoice, int borne = int.MaxValue)
        {
            Console.Write("\n" + message);

            string saisi = Console.ReadLine();
            if (int.TryParse(saisi, out userChoice))
            {
                return IsInBorne(userChoice, borne);
            }
            else
            {
                Console.WriteLine("Invalide, reboot... ");
                return false;
            }
        }
        static bool Saisir(string message, out float userChoice, float borne = float.MaxValue)
        {
            Console.Write("\n" + message);
            string saisi = Console.ReadLine();
            if (float.TryParse(saisi, out userChoice))
            {
                return IsInBorne(userChoice, borne);
            }
            else
            {
                Console.WriteLine("Invalide, reboot... ");
                return false;
            }
        }
        static bool IsInBorne(float choix, float borne)
        {
            if (choix < 1 || choix > borne)
            {
                Console.WriteLine("Choix invalide !");
                return false;
            }
            return true;
        }
        static void PrintBanner(string banner, ConsoleColor color = ConsoleColor.Cyan)
        {
            Console.ForegroundColor = color;
            Console.WriteLine(banner);
            Console.ResetColor();
        }
    }
}
