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
            while (true)
            {
                if (!Saisir("===  Test_App  === \n1: Calculatrice \n2: Juste Prix \n3: Quitter \nChoix: ", out int ActionChoice, 3))
                {
                    continue;
                }
                    
                switch (ActionChoice)
                {
                    case 1:
                        //Calculatrice
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
                        Random random = new Random();
                        int nbGuess = 5;
                        int randomMax = 51;
                        bool hasWon = false;

                        int valueToGuess = random.Next(0, randomMax);
                        while (nbGuess > 0 && !hasWon)
                        {
                            if (Saisir("Ton guess: ", out int guess, randomMax))
                            {
                                if (guess == valueToGuess - 1 || guess == valueToGuess || guess == valueToGuess + 1)
                                {
                                    hasWon = true;
                                    Console.WriteLine("Tu as gagné !");
                                }
                                else
                                {
                                    Console.WriteLine(valueToGuess > guess ? "La valeur est supérieur" : "La valeur est inférieur");
                                }
                            }
                            else
                            {
                                continue;
                            }

                            nbGuess--;
                            Console.WriteLine(nbGuess + " / 5 essai(s) restant(s). ");
                        }

                        Console.WriteLine("Fin du jeu, merci d'y avoir joué ! La valeur était : " + valueToGuess);
                        break;

                    case 3:
                        //Quit
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
    }
}
