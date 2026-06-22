using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Random;
namespace Juste_prix
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Random al = new Random();
            int aleatoire = al.Next(0, 51);
            int UserGuess = 5;
            Console.WriteLine(aleatoire);
            while (UserGuess > 0) ;
            {
                string message = "Ton guess: ";

                if (UserGuess == aleatoire - 1 || UserGuess == aleatoire || UserGuess == aleatoire + 1) ;
                {

                }
            }
        }
    }
}
