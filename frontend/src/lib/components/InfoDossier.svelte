<script lang="ts" context="module">
	export type Fichier = { name: string; status: 'complete' | 'pending' | 'rejected' };
</script>

<script lang="ts">
	import {
		Avatar,
		Card,
		Badge,
		Button,
		Progressbar,
		Dropdown,
		DropdownItem
	} from 'flowbite-svelte';
	import { GlobeOutline, CloudArrowUpOutline, DotsVerticalOutline } from 'flowbite-svelte-icons';

	export let nom: string = 'Dossier sans nom';
	export let transport: 'maritime' | 'aérien' | '?' = '?';
	export let fichiers: Fichier[] = [];
	const progress = (fichiers.filter((f) => f.status === 'complete').length / fichiers.length) * 100;
</script>

<Card padding="xs" class="relative mt-4">
	{#if progress === 100}
		<div class="absolute flex h-full w-full items-center justify-center">
			<p class="rotate-12 rounded border-4 border-green-600 p-2 text-center text-6xl font-bold text-green-600">COMPLET</p>
		</div>
	{/if}
	<div class="flex justify-start border-b">
		<Avatar class="mr-3 p-1">
			{#if transport === 'maritime'}
				<GlobeOutline />
			{:else if transport === 'aérien'}
				<CloudArrowUpOutline />
			{:else}
				{transport}
			{/if}
		</Avatar>
		<h3 class="mb-4 text-2xl font-bold w-full">{nom}</h3>
		<DotsVerticalOutline size="lg" class="hover:bg-slate-50 rounded-full" id="fdrop" />
	</div>
	<div class="flex flex-wrap space-x-2 pt-2">
		{#each fichiers as { name, status }}
			{@const color = status === 'complete' ? 'green' : status === 'rejected' ? 'red' : 'dark'}
			<Badge {color} class="w-fit rounded-full px-3 py-1">{name}</Badge>
		{/each}
	</div>
	<Progressbar class="mt-6" progressClass="bg-sky-400" {progress} />
</Card>

<Dropdown triggeredBy="#fdrop">
    <DropdownItem>Compléter le dossier</DropdownItem>
    <DropdownItem>Voir détails</DropdownItem>
</Dropdown>