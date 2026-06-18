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
        public int choix;
        public int borne;
        static void Main(string[] args)
        {
            Operation[5] operations = new Operation[5];
            while (true)
            {
                Console.WriteLine("~~~~[1]: Opérateur~~~~ \n~~~~[2]: Puissances~~~ \n~~~~[3]: Fonctions~~~~ \n~~~~[4]: Quit~~~~~~~~~");
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
                        Console.WriteLine("~~~~Opérateur~~~~ \n==[1]: + \n==[2]: - \n==[3]: * \n==[4]: / \n==[5]: // \n==[6]: %");
                        int operateur = Convert.ToInt32(Console.ReadLine());
                        Console.Write("a: ");
                        float a = Convert.ToSingle(Console.ReadLine());
                        Console.Write("b: ");
                        float b = Convert.ToSingle(Console.ReadLine());
                        if (!IsInBorne(operateur, 6))
                        {
                            continue;
                        }

                        break;
                    case 2:

                        break;
                    case 3:

                        break;
                    case 4:
                        Console.WriteLine("Au revoir !");
                        return;
                }
            }
          
        }
        static bool IsInBorne(int choix, int borne)
        {
            if (choix < 0 || choix > borne)
            {
                global::System.Console.WriteLine("Choix invalide !");
                return false;
            }
            else
            {
                return true;
            }
        }
        public abstract class Operation
        {
            public abstract float Calcul(float a, float b);
        }
        public class Addition : Operation
        {
            public override float Calcul(float a, float b)
            {
                return a + b;
            }
        }
    }
}
