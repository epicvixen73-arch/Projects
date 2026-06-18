using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Math = System.Math;
namespace Calculatrice
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
                return a / 1;
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

            List<Operation> operations = new List<Operation>();
            operations.Add(new Addition());
            operations.Add(new Soustraction());

            List<Fonctions> fonctions = new List<Fonctions>();
            fonctions.Add(new Carre());
            fonctions.Add(new Cube());
            fonctions.Add(new Inverse());
            fonctions.Add(new Racine());
            fonctions.Add(new Absolue());


            while (true)
            {
                Console.WriteLine("-----[1]: Opérateur---- \n-----[2]: Puissances--- \n-----[3]: Fonctions---- \n-----[4]: Quit---------");
                Console.Write("Choix: ");
                int choix = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine();
                if  (!IsInBorne(choix, 4))
                {
                    continue;
                }
                switch (choix)
                {
                    case 1:
                        Console.WriteLine("-------Opérateur-------");
                        for (int i = 0; i < operations.Count; i++)
                        {
                            Operation op = operations[i];
                            Console.WriteLine("[" + (i+1) + "] " + op.GetName());
                        }
                        
                        int operateur = Convert.ToInt32(Console.ReadLine());
                        if (!IsInBorne(operateur, operations.Count))
                        {
                            continue;
                        }
                        Console.WriteLine("-----------------------");
                        Console.Write("a: ");
                        float a = Convert.ToSingle(Console.ReadLine());
                        Console.Write("b: ");
                        float b = Convert.ToSingle(Console.ReadLine());
                        Console.WriteLine();
                        Console.WriteLine("Result: " + operations[operateur-1].Calcul(a,b ));
                        Console.WriteLine("#######################");
                        break;
                    case 2:
                        
                        break;
                    case 3:
                        Console.WriteLine("-------Fonctions-------");
                        for (int i = 0; i < fonctions.Count; i++)
                        {
                            Fonctions op = fonctions[i];
                            Console.WriteLine("[" + (i + 1) + "] " + op.GetName());
                        }

                        int fonc = Convert.ToInt32(Console.ReadLine());
                        if (!IsInBorne(fonc, fonctions.Count))
                        {
                            continue;
                        }
                        Console.WriteLine("-----------------------");
                        Console.Write("a: ");
                        a = Convert.ToSingle(Console.ReadLine());
                        Console.WriteLine();
                        Console.WriteLine("Result: " + fonctions[fonc - 1].Fonction(a));
                        Console.WriteLine("#######################");
                        break;
                    case 4:
                        Console.WriteLine("Au revoir !");
                        return;
                }
            }
          
        }
        static bool IsInBorne(int choix, int borne)
        {
            if (choix < 1 || choix > borne)
            {
                global::System.Console.WriteLine("Choix invalide !");
                return false;
            }
            else
            {
                return true;
            }
        }
        
    }
}
