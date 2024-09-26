<script>
  import { Alert, Card } from 'flowbite-svelte';
</script>

<div class="p-8">
  <Alert dismissable>
    <span class="font-medium">Info alert!</span>
    Juste pour vérifier que ça marche !
  </Alert>
  <h1>Liens utiles</h1>

  <Card>Pour une meilleure gestion de la réactivité: <a href="https://svelte.dev">Svelte</a></Card>
  <Card>Pour une meilleure expérience de l'utilisation du framework: <a href="https://kit.svelte.dev">SvelteKit</a></Card>
  <Card>Bootstrap c'est du passé svp. Tailwind est pur: <a href="https://tailwindcss.com/">Tailwindcss</a></Card>
  <Card>Pour templates et autres components...<a href="https://flowbite-svelte.com/">Flowbite</a></Card>
</div>

<style lang="postcss">
    a {
        @apply text-blue-800 underline;
    }
</style>