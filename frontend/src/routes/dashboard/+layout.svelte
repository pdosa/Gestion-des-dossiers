<script lang="ts">
	import { page } from '$app/stores';
	import Notifications from '$lib/components/Notifications.svelte';
	import {
		Sidebar,
		SidebarBrand,
		SidebarGroup,
		SidebarItem,
		SidebarWrapper,
		Navbar,
		Dropdown,
		DropdownItem,
		DropdownDivider
	} from 'flowbite-svelte';
	import {
		BellSolid,
		ChartPieSolid,
		HomeSolid,
		FileSolid,
		ArrowRightToBracketOutline,
		EditOutline
	} from 'flowbite-svelte-icons';
	let spanClass = 'flex-1 ms-3 whitespace-nowrap';
	$: activeUrl = $page.url.pathname;

	let notifications = [
		{ id: 1, message: 'Document ajouté au Dossier 001', lu: false },
		{ id: 2, message: 'Dossier 002 validé', lu: true }
	];
	function markAsRead(id: number) {
		notifications = notifications.map((notif) =>
			notif.id === id ? { ...notif, lu: true } : notif
		);
	}
</script>

<div class="flex h-full bg-white">
	<Sidebar
		class="h-full min-w-max bg-slate-50"
		asideClass="w-52"
		nonActiveClass="flex items-center p-2 text-base font-normal text-slate-900 bg-white rounded-lg dark:text-white hover:bg-slate-100 dark:hover:bg-slate-700;"
		{activeUrl}
	>
		<SidebarWrapper>
			<SidebarGroup>
				<SidebarBrand
					imgClass="mx-auto h-11 mb-10"
					aClass="none"
					site={{ name: '', href: '', img: '/logo-sm.png' }}
				/>
				<SidebarItem label="Dashboard" href="/dashboard">
					<svelte:fragment slot="icon">
						<HomeSolid
							class="h-6 w-6 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
						/>
					</svelte:fragment>
				</SidebarItem>
				<SidebarItem label="Dossier" href="/dashboard/dossiers" {spanClass}>
					<svelte:fragment slot="icon">
						<FileSolid
							class="h-6 w-6 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
						/>
					</svelte:fragment>
					<svelte:fragment slot="subtext">
						<span
							class="text-primary-600 bg-primary-200 dark:bg-primary-900 dark:text-primary-200 ms-3 inline-flex h-3 w-3 items-center justify-center rounded-full p-3 text-sm font-medium"
						>
							1
						</span>
					</svelte:fragment>
				</SidebarItem>
				<SidebarItem label="Déconnexion" href="/">
					<svelte:fragment slot="icon">
						<ArrowRightToBracketOutline
							class="h-6 w-6 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
						/>
					</svelte:fragment>
				</SidebarItem>
				<SidebarItem label="Profil" href="/dashboard/profiles">
					<svelte:fragment slot="icon">
						<EditOutline
							class="h-6 w-6 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white"
						/>
					</svelte:fragment>
				</SidebarItem>
			</SidebarGroup>
		</SidebarWrapper>
	</Sidebar>

	<div class="w-full">
		<Navbar fluid>
			<div class="text-gray-400">
				<h1 class="mb-2 text-5xl font-extrabold">Dashboard</h1>
				<p>Bon retour | Nom utitlisateur</p>
			</div>
			<BellSolid
				size="xl"
				title={{ id: 'N', title: 'Notifications' }}
				color="gray"
				id="notif-drop"
			/>
			<Dropdown triggeredBy="#notif-drop">
				{#each notifications as notification}
					<DropdownDivider />
					<DropdownItem>
						<p>{notification.message}</p>
						<button
							on:click={() => markAsRead(notification.id)}
							class="mt-2 text-[001C98] underline hover:text-[F02532]">Marquer comme lu</button
						>
					</DropdownItem>
				{/each}
			</Dropdown>
		</Navbar>
		<div class="mt-4 h-full w-full px-2">
			<slot></slot>
		</div>
	</div>
</div>
