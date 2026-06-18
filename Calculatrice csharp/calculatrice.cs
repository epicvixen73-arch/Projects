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
        static void Main(string[] args)
        {
            Console.WriteLine("~~~~[1]: Opérateur~~~~ \n~~~~[2]: Puissances~~~ \n~~~~[3]: Fonctions~~~~");
            Console.Write("Choix: ");
            int choix = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine();
            if (choix < 0 || choix > 3)
            {
                Console.WriteLine("Choix invalide !");
            }
            switch (choix)
            {
                case 1:
                    Console.WriteLine("~~~~Opérateur~~~~ \n==[1]: + \n==[2]: - \n==[3]: * \n==[4]: / \n==[5]: // \n==[6]: %");
                    int opérateur = Convert.ToInt32(Console.ReadLine());
                    if (choix < 0 || choix > 6)
                    {
                       
                    }
                    break;
                case 2:
                    
                    break;
                case 3:
                    
                    break;
            }
        }
        //public bool FiltreBorne(int borne)
        //{
        //    if (choix < 0 || choix > borne)
        //    {
        //        global::System.Console.WriteLine("test true");
        //        return false;
        //    }
        //    else
        //    {
        //        global::System.Console.WriteLine("test false");
        //        return true;
        //    }
        //}

    }
}
