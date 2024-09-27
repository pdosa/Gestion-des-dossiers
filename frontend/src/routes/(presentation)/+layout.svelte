<header title="votre header ici">
    <ul class="py-3 flex justify-around shadow-sm">
        <li>Un <a href="/">lien</a></li>
        <li>Un <a title="Créez une balise avec l'id `section` et le lien pointera vers là" href="#section">lien vers un section de la page</a></li>
        <li><a title="Petit raccourci vers le dashboard (pour gagner en temps!)" href="/dashboard">Dashboard</a></li>
    </ul>
</header>

<slot></slot>

<footer class="text-center py-5 shadow">
    By PDO <br/>
    @Copyright 2024. Tous droits réservés.
</footer>