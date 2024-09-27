<script lang="ts" context="module">
    export type Fichier = { name: string; status: "complete" | "pending" | "rejected" };
</script>
<script lang="ts">
    import { Avatar, Card, Badge } from 'flowbite-svelte';
    import { GlobeSolid, LightbulbSolid } from 'flowbite-svelte-icons';

    export let nom: string = "Dossier sans nom";
    export let transport: "maritime" | "aérien" | "?" = "?";
    export let fichiers: Fichier[] = [];
</script>

<Card padding="xs">
    <div class="flex justify-start border-b">
        <Avatar class="p-1 mr-3">{transport}</Avatar>
        <h3 class="font-bold text-2xl mb-4">{nom}</h3>
    </div>
    <div class="flex flex-wrap space-x-2 pt-2">
        {#each fichiers as { name, status }}
            {@const color = status === "complete" ? "green": status ==="rejected" ? "red" : "dark"}
            <Badge {color} class="w-fit py-1 px-3 rounded-full">{name}</Badge>
        {/each}
    </div>
    <div class="mt-10 w-80 h-2 bg-gray-200 rounded-full">
        <div class="w-[30%] h-2 bg-sky-300 rounded-full"></div>
    </div>
</Card>
